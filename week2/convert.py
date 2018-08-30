import csv
import json
import random

fileName = './login-logout.csv'

csvfile = open(fileName)
reader = csv.DictReader(csvfile)
date = {}

for row in reader:
    data = { 
        "login": int(row['#login']), 
        "logout": int(row['#logout'])
    }
    date[row['time']] = data

#print(date)
print(json.dumps(date))