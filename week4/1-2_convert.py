import csv
import json
import random
from collections import OrderedDict

fileName = './1-2.csv'

csvfile = open(fileName)
reader = csv.DictReader(csvfile)
data = {}
all = []

for row in reader:
    value = round(float(row['#Request'])/4799*100,2)
    name = row['User']+'\n\n'+str(value)+'%'
    data = { 
        "value": value,
        "name": name
    }
    all.append(data)

#data = OrderedDict(sorted(data.items(), key=lambda t: t[0]))
print(json.dumps(all))