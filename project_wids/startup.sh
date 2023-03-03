#!/bin/bash

python3 /home/pi/project_wids/modesetup.py
sudo dhcpcd
mount -t tmpfs -o size=512M tmpfs /home/pi/project_wids/data

/home/pi/project_wids/2.4ghz_script.sh &> /dev/null &
/home/pi/project_wids/5ghz_script.sh &> /dev/null &


