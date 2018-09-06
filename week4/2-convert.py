import csv
import json
import random
from collections import OrderedDict

fileName = './2.csv'

csvfile = open(fileName)
reader = csv.DictReader(csvfile)
data = []
all = []

for row in reader:
    data = [row['time'],row['user'],row['ip_src'],row['ip_dst'],row['port_dst'],row['hostname']]
    all.append(data)

#data = OrderedDict(sorted(data.items(), key=lambda t: t[0]))
print(json.dumps(all))