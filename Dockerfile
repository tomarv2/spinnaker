FROM alpine

#ENV HOME=/config

RUN apk add --update \
    ca-certificates \
    groff \
    less \
    python \
    py-pip \
    curl

ADD https://storage.googleapis.com/kubernetes-release/release/v1.6.4/bin/linux/amd64/kubectl /usr/local/bin/kubectl

RUN set -x && \
    apk add --no-cache curl ca-certificates && \
    chmod +x /usr/local/bin/kubectl && \
    adduser kubectl -Du 2342 -h /config && \
    kubectl version --client && \
    pip install awscli

