#!/usr/bin/python
import csv, sys, json, elasticsearch
from elasticsearch import helpers

es           = elasticsearch.Elasticsearch()
csvfile      = '2014-03-12.csv'
jdata        = dict()
actions      = list()
i            = 0
proto        = {'0': '0', '1': 'ICMP', '2': 'IGMP', '6': 'TCP', '17': 'UDP', '112': 'VRRP', '3': 'GGP', '46': 'RSVP', '50': 'ESP'}

with open(csvfile, 'rb') as file :
	line = csv.reader(file, delimiter = ',', skipinitialspace = True)
	for row in line :
		i += 1
		jdata = { 'ts': row[0][0:19], 'byte': int(row[5]), 'sa': row[1], 'sp': int(float(row[2])), 'da': row[3], 'dp': int(float(row[4])), 'pkt': int(row[6]), 'out': int(row[7]), 'pr': proto[row[8].strip()] }
		action = { '_index': 'tuned', '_type': 'fnf3x', '_id': i, '_source': json.dumps(jdata, separators=(',', ':'))}
		actions.append(action)
		if i % 100000 == 0:
			elasticsearch.helpers.bulk(es, actions)
			print "Indexed %d, working on next 100000" %(i)
			actions = list()
	elasticsearch.helpers.bulk(es, actions)
	print "Indexed %d, finishing." %(i)
