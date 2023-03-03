#!/usr/bin/env python3

import time, json
import pandas as pd
from datetime import datetime

def parser():
	f = open("/home/pi/project_wids/data/2.4ghz_data.json")
	data = json.load(f)
	output=list()
	output2=list()
	i=0
	for row in data:
		d=dict()
		for key in row:
			row[key]=str(row[key]).strip()
			if key == " Last time seen" or " First time seen":
				try:
					TS = time.mktime(time.strptime(row[key], '%Y-%m-%d %H:%M:%S'))
					row[key]=int(TS)
				except:
					pass
			akey = key.strip()
			if not key == ' LAN IP':
				d[akey]=row[key]
		if not d['BSSID']=='Station MAC' and i==0:
			output.append(d)
		elif i==1:
			output2.append(d)
		else:
			i=1

	out=dict()
	out['FREQ']='2.4GHz'
	out['APS']=output
	out['CLIENT']=output2

	f.close()
	with open('/home/pi/project_wids/data/2.4ghz_dataparsed.json', 'w') as outfile:
		json.dump(out, outfile)
		outfile.close()

def converser():
	print("\nConverting .CSV file to .JSON...")
	csv_file = pd.DataFrame(pd.read_csv(r"/home/pi/project_wids/data/2.4ghz_data-01.csv",
				sep=",", header=0, index_col=False))
	csv_file.to_json(r"/home/pi/project_wids/data/2.4ghz_data.json", orient="records",
			date_format="epoch", double_precision=10, force_ascii=True,
			date_unit="ms", default_handler=None)
	time.sleep(1)
	print("Conversion done.")


def main():
	converser()
	time.sleep(1)
	parser()

if __name__=="__main__":
	main()

