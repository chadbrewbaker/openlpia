import csv
import os
with open('/tmp/ipman.csv', 'rb') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
	for row in spamreader:
                print row
                #uri = row[0]
		#os.system("curl -i --basic " + uri + " > _"+uri)
