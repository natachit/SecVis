import csv
import json
import random

csvfile = open('./2018-07-Domestic Exchange.csv')
reader = csv.DictReader(csvfile)
nodes = []
edges = []
allNode = {}
source = {}
for row in reader:
    if row['ASN-source'] not in source:
        source[row['ASN-source']] = float(row['Bandwidth'])
    else:
        source[row['ASN-source']] += float(row['Bandwidth'])
    edge = {
        "sourceID": row['ASN-source'], 
        "attributes": {}, 
        "targetID": row['ASN'], 
        "size": row['Bandwidth']
    }
    edges.append(edge)


csvfile = open('./2018-07-Domestic Exchange.csv')
reader = csv.DictReader(csvfile)
for row in reader:
    asn = row['ASN']
    if asn not in allNode:
        size = float(row['Bandwidth'])/10
        r = lambda: random.randint(0,255)
        colorRan = '#%02X%02X%02X' % (r(),r(),r())
        if asn in source:
            size = source[asn]/10
        node = {
            'color': colorRan,
            'label': row['Name'],
            'attributes': {},
            'x': random.randint(-2000,2000),
            'y': random.randint(-900,900),
            'id': row['ASN'],
            'size': size
        }
        nodes.append(node)
        allNode[row['ASN']] = row['Name']



data = {
    "nodes": nodes,
    "edges": edges,
}
print(source)
#print(json.dumps(data))
