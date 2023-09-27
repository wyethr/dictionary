#!/usr/bin/env python3

import csv 
import json

class Term: 
	def __init__(self, word, greenNotes, ambidextrous, farmerHenley, lastDate):
		self.word = word
		self.greenNotes = greenNotes

		if ambidextrous == "Y":
			self.ambidextrous = "true"
		else: 
			self.ambidextrous = "false"

		if farmerHenley == "Y":
			self.farmerHenley = "true"
		else: 
			self.farmerHenley = "false"

		self.firstDate = 2023
		self.lastDate = lastDate
		self.yearsUsed = 0

		# self.dictionaryEntry = '{ "word": "' + self.word + '", "usageNumber": ' + self.usageNumber + ', "greenNotes": "' + self.greenNotes + '", "ambidextrous": ' + self.ambidextrous + ', "farmerHenley": ' + self.farmerHenley + ', "firstDate": ' + self.firstDate + ', "lastDate": ' + self.lastDate + ', "yearsUsed": ' + self.yearsUsed + '}'

		self.usage = []

		with open('masculineUsage.csv', newline='') as csvfile:
			spamreader = csv.reader(csvfile)

			for row in spamreader:
				if row[0] != "" and row[0] != "Word" and row[0] == self.word:
					add = {
						"date": row[1],
						"notesCitation": row[2],
						"greenCitation": row[3],
						"citation": row[4]
					}

					if int(row[1]) < int(self.firstDate):
						self.firstDate = row[1]

					self.usage.append(add)

		self.usageNumber = len(self.usage)

		if self.lastDate != "":
			self.yearsUsed = int(self.lastDate) - int(self.firstDate)

		if self.farmerHenley:
			self.usageNumber += 1

		self.dictionaryEntry = { 
			"word": self.word, 
			"usageNumber": self.usageNumber,
			"greenNotes": self.greenNotes, 
			"ambidextrous": self.ambidextrous,
			"farmerHenley": self.farmerHenley,
			"firstDate": self.firstDate, 
			"lastDate": self.lastDate,
			"yearsUsed": self.yearsUsed,
			"usage": self.usage
		}

masculineTerms = []

with open('masculineTerms.csv', newline='') as csvfile:
	spamreader = csv.reader(csvfile)

	for row in spamreader:
		if row[0] != "" and row[0] != "Word":
				add = Term(row[0], row[2], row[3], row[4], row[6])
				masculineTerms.append(add.dictionaryEntry)

print(json.dumps(masculineTerms))
