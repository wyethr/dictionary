#!/usr/bin/env python3

## ./hello_csv.py to run
## or:
## python3 hello_csv.py


import csv
import json

with open('usage.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile)
    for row in spamreader:
        print(row[0])

