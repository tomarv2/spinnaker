import os

cmd_to_run = "" \
'''hal config provider docker-registry account edit dcr-docker-registry \
                             --address https://dcr.demo.com \
                             --username devops \
                             --cache-interval-seconds 600 \
                             --repositories \
demo/island,\
demo/services/config-builder \
--password 
'''

# hal deploy apply --service-names=clouddriver