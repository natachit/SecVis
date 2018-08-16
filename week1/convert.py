import csv
import json
import random

#fileName = './2018-07-International Exchange.csv'
fileName = './2018-07-Domestic Exchange.csv'

csvfile = open(fileName)
reader = csv.DictReader(csvfile)
nodes = []
edges = []
allNode = {}
source = {}
for row in reader:
    if row['ASN-source'] not in source:
        source[row['ASN-source']] = 20
    else:
        source[row['ASN-source']] += 2
    edge = {
        "sourceID": row['ASN-source'], 
        "attributes": {}, 
        "targetID": row['ASN'], 
        "size": row['Bandwidth']
    }
    edges.append(edge)


csvfile = open(fileName)
reader = csv.DictReader(csvfile)
for row in reader:
    asn = row['ASN']
    if asn not in allNode:
        r = lambda: random.randint(0,255)
        colorRan = '#%02X%02X%02X' % (r(),r(),r())
        if asn in source:
            size = source[asn]
        else:
            size = 10
        node = {
            'color': colorRan,
            'label': row['Name'],
            'attributes': {},
            'x': random.randint(-2000,2000),
            'y': random.randint(-1000,1000),
            'id': row['ASN'],
            'size': size
        }
        nodes.append(node)
        allNode[row['ASN']] = row['Name']



data = {
    "nodes": nodes,
    "edges": edges,
}
#print(source)
print(json.dumps(data))