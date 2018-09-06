import csv
import json
import random
from collections import OrderedDict

fileName = './1-1.csv'

csvfile = open(fileName)
reader = csv.DictReader(csvfile)
data = {}

for row in reader:
    a = int(row['count'])
    data[row['time']] = a
data = OrderedDict(sorted(data.items(), key=lambda t: t[0]))
print(json.dumps(data))