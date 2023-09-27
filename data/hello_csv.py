#!/usr/bin/env python3

## ./hello_csv.py to run
## or:
## python3 hello_csv.py
## chmod +x "name of file" 
## ls -l to see characteristics
## mv "current document name" "what you want to change it to"


import csv
import json

with open('masculineUsage.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile)
    for row in spamreader:
        print(row[0])

