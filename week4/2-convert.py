import csv
import json
import random
from collections import OrderedDict

fileName = './2.csv'

csvfile = open(fileName)
reader = csv.DictReader(csvfile)
data = []
all0 = []
all1 = []
all2 = []
all3 = []
all4 = []
user = ['RMUn6owxz3Npjow@ku.ac.th',
        'RMUjtMPNJ6aT3TB@ku.ac.th',
        'RMUpKGYn9d5by4N@ku.ac.th',
        'RMUpKmcaiQtXA57@ku.ac.th',
        'RMUkdLcDsnd6MSH@ku.ac.th']

for row in reader:
    if row['user'] == user[0]:
        data = [row['time'],row['user'],row['ip_src'],row['ip_dst'],row['port_dst'],row['hostname']]
        all0.append(data)
    elif row['user'] == user[1]:
        data = [row['time'],row['user'],row['ip_src'],row['ip_dst'],row['port_dst'],row['hostname']]
        all1.append(data)
    elif row['user'] == user[2]:
        data = [row['time'],row['user'],row['ip_src'],row['ip_dst'],row['port_dst'],row['hostname']]
        all2.append(data)
    elif row['user'] == user[3]:
        data = [row['time'],row['user'],row['ip_src'],row['ip_dst'],row['port_dst'],row['hostname']]
        all3.append(data)
    elif row['user'] == user[4]:
        data = [row['time'],row['user'],row['ip_src'],row['ip_dst'],row['port_dst'],row['hostname']]
        all4.append(data)

#data = OrderedDict(sorted(data.items(), key=lambda t: t[0]))
print(json.dumps(all0))
print("\n\n\n----------------------------------------------\n\n\n")
print(json.dumps(all1))
print("\n\n\n----------------------------------------------\n\n\n")
print(json.dumps(all2))
print("\n\n\n----------------------------------------------\n\n\n")
print(json.dumps(all3))
print("\n\n\n----------------------------------------------\n\n\n")
print(json.dumps(all4))