#!/bin/bash

# crontab - if this file is cron_cmd
# */5 8-22 * * 1-5 /home/akhan/retrieve_cfmm/cron_cmd

/home/akhan/retrieve_cfmm/check_and_remote_retrieve.py akhanf graham.sharcnet.ca ~/.ssh/id_rsa_graham.sharcnet.ca /project/6007967/akhanf/autobids-cfmm/bin/procNewScans 2>&1 1>/dev/null | /usr/bin/logger -t "retrieve_cfmm"
