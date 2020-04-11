#!/usr/bin/env groovy

pipeline {
    options {
      disableConcurrentBuilds()
      buildDiscarder(logRotator(numToKeepStr: '5'))
    }
    agent { label 'infra' }
    stages {
        stage('Prepare Build') {
            when {
                anyOf {
                    branch "master"
                }
            }
            steps {
                // grab info from pom file
                script {
                    env.nameSpace = "sharedservices"
                }
                checkout scm
                sh "git rev-parse --short HEAD > .git/commit-id"
            }
        }
        stage('Update Configmap') {
            when {
                anyOf {
                    branch "master"
                }
            }
            steps {
                withCredentials([usernamePassword(credentialsId: 'k8s_cluster_pwd_prod', passwordVariable: 'k8s_pwd', usernameVariable: 'k8s_user')]) {
                    sh "kubectl --server='https://k8s-master.tomarv2.com' --username=${k8s_user} --password=${k8s_pwd} --insecure-skip-tls-verify=true -n ${env.NameSpace} create configmap spinnaker-halyard --from-file=config/aws_config.yaml --from-file=config/hal_config.yaml --from-file=config/kube_config.yaml --dry-run -o yaml | kubectl --server='https://k8s-master.tomarv2.com' --username=${k8s_user} --password=${k8s_pwd}  --insecure-skip-tls-verify=true -n ${env.NameSpace} replace -f - "
                    sh "aws ecr get-login --include-email |cut -f6 -d ' ' > ecr-secret-token"
                    sh "tr -d '\n' < ecr-secret-token | tee ecr-secret-token"
                    sh "cat ecr-secret-token"
                }
            }
        }
        stage('Patch Secret') {
            when {
                anyOf {
                    branch "master"
                }
            }
            steps {
                withCredentials([usernamePassword(credentialsId: 'k8s_cluster_pwd_prod', passwordVariable: 'k8s_pwd', usernameVariable: 'k8s_user')]) {
                    sh "kubectl --server='https://k8s-master.tomarv2.com' --username=${k8s_user} --password=${k8s_pwd} --insecure-skip-tls-verify=true -n ${env.NameSpace} create secret generic halyard-ecr-secret --from-file=ecr-secret-token --dry-run -o yaml | kubectl --server='https://k8s-master.tomarv2.com' --username=${k8s_user} --password=${k8s_pwd}  --insecure-skip-tls-verify=true -n ${env.NameSpace} replace -f - "
                }
            }
        }
        stage('Delete Halyard pod') {
            when {
                anyOf {
                    branch "master"
                }
            }
            steps {
                withCredentials([usernamePassword(credentialsId: 'k8s_cluster_pwd_prod', passwordVariable: 'k8s_pwd', usernameVariable: 'k8s_user')]) {
                    sh "kubectl --server='https://k8s-master.tomarv2.com' --username=${k8s_user} --password=${k8s_pwd} --insecure-skip-tls-verify=true -n ${env.NameSpace} get pods -n sharedservices -l app=halyard -o json  | jq -r '.items[] | [.metadata.name] | sort[]' | tail -1 > POD_NAME"
                    script {
                        env.POD_NAME = sh(returnStdout: true, script: 'cat POD_NAME').trim()
                    }
                    sh "echo ${env.POD_NAME}"
                    sh "kubectl --server='https://k8s-master.tomarv2.com' --username=${k8s_user} --password=${k8s_pwd} --insecure-skip-tls-verify=true -n ${env.NameSpace} -n sharedservices delete pod ${env.POD_NAME}"
                    sh "sleep 90"
                }
            }
        }
        stage('Secrets') {
            when {
                anyOf {
                    branch "master"
                }
            }
            steps {
                withCredentials([usernamePassword(credentialsId: 'k8s_cluster_pwd_prod', passwordVariable: 'k8s_pwd', usernameVariable: 'k8s_user')]) {
                    sh "kubectl --server='https://k8s-master.tomarv2.com' --username=${k8s_user} --password=${k8s_pwd} --insecure-skip-tls-verify=true -n ${env.NameSpace} get pods -n sharedservices -l app=halyard -o json  | jq -r '.items[] | [.metadata.name] | sort[]' | tail -1 > POD_NAME_UPDATED"
                    script {
                        env.POD_NAME_UPDATED = sh(returnStdout: true, script: 'cat POD_NAME_UPDATED').trim()
                    }
                    sh "echo ${env.POD_NAME_UPDATED}"
                    sh "sleep 60"
                }
            }
        }
        stage('Restart Clouddriver') {
            when {
                anyOf {
                    branch "master"
                }
            }
            steps {
                withCredentials([usernamePassword(credentialsId: 'k8s_cluster_pwd_prod', passwordVariable: 'k8s_pwd', usernameVariable: 'k8s_user')]) {
                    sh "kubectl --server='https://k8s-master.tomarv2.com' --username=${k8s_user} --password=${k8s_pwd} --insecure-skip-tls-verify=true -n ${env.NameSpace}  exec ${env.POD_NAME_UPDATED} -- bash -c 'hal deploy apply --service-names=clouddriver'"
                }
            }
        }
    }
    post {
        always {
            writeFile file: "build.properties", text: "NAMESPACE=${env.NameSpace}"
            archiveArtifacts 'build.properties'
            cleanWs()
        }
    }
}


@NonCPS
def static cleanBranchName(String branchName) {
    return branchName.replaceAll("/", "-")
}

@NonCPS
def getChangeString() {
    MAX_MSG_LEN = 100
    def changeString = ""

    echo "Gathering SCM changes"
    def changeLogSets = currentBuild.changeSets
    for (int i = 0; i < changeLogSets.size(); i++) {
        def entries = changeLogSets[i].items
        for (int j = 0; j < entries.length; j++) {
            def entry = entries[j]
            truncated_msg = entry.msg.take(MAX_MSG_LEN)
            changeString += " - ${truncated_msg} [${entry.author}]\n"
        }
    }

    if (!changeString) {
        changeString = " - No new changes"
    }
    return changeString
}


