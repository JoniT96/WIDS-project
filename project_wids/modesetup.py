#!/usr/bin/env python3

import time, subprocess

iwconfig = subprocess.check_output("iwconfig", encoding="ASCII")
lista=list()

for adapters in iwconfig.split("\n"):
	asd=adapters.split(' ')
	for adapter in asd:
		if "wlan" in adapter:
			lista.append(adapter)
print(lista)

print("\nKilling interfering processes...")
subprocess.call("airmon-ng check kill",shell=True)
print("Done. Enabling monitor mode for wlan adapters...")
for adap in lista:
	subprocess.call("ifconfig "+adap+" down",shell=True)
	time.sleep(1)
	subprocess.call("iwconfig "+adap+" mode monitor",shell=True)
	time.sleep(1)
	subprocess.call("ifconfig "+adap+" up",shell=True)
	print("\nDone. Monitor mode enabled for "+adap+".")
