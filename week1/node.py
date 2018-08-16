import csv
import json
import random

filename = ('./2018-07-International Exchange.csv'
csvfile = open(filename)
reader = csv.DictReader(csvfile)
nodes = []
edges = []
allNode = {}
source = {}
for row in reader:
    a = row['ASN-source']
    b = row['ASN']
    if a not in nodes:
        nodes.append(a)
    if b not in nodes:
        nodes.append(b)

print(len(nodes))
    
