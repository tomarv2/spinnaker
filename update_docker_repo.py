import os

cmd_to_run = "" \
'''hal config provider docker-registry account edit dcr-docker-registry \
                             --address https://dcr.tomarv2.com \
                             --username devops \
                             --cache-interval-seconds 600 \
                             --repositories \
tomarv2/island,\
tomarv2/services/config-builder \
--password 
'''

# hal deploy apply --service-names=clouddriver