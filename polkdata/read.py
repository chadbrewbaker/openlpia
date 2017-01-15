import csv
import os
with open('clintonmail.csv', 'rb') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=':', quotechar='|')
	for row in spamreader:
                uri = row[0]
		os.system("curl -i --basic " + uri + " > _"+uri)
