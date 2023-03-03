#!/bin/bash

while [ 1 ]
do
	airodump-ng -M -w /home/pi/project_wids/data/5ghz_data wlan2 --berlin 30 -b a &
	PID=$!
	sleep 10
	kill -9 $PID
	python3 /home/pi/project_wids/5ghz_main.py
	sleep 5
	nc -u 10.69.2.230 10000 < /home/pi/project_wids/data/5ghz_dataparsed.json -w 2
	sleep 5
	rm /home/pi/project_wids/data/5ghz_data* -f
done
