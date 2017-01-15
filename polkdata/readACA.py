import csv
import os
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.ticker import FuncFormatter
stuff =[]

def millions(x, pos):
        'The two args are the value and tick position'
        return '$'+ str(x)
formatter = FuncFormatter(millions)


def num(s):
        try:
            return float(s)
        except ValueError:
            return 0

with open('ACA.csv', 'rb') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
	for row in spamreader:
                uri = row[7]
                uri = uri.translate(None, '!@#$')
                stuff = stuff +[num(uri)]
		print uri
                #os.system("curl -i --basic " + uri + " > _"+uri)

print stuff
data = np.array(stuff) 

# fixed bin size
bins = np.arange(min(data), max(data), 20) # fixed bin size

plt.xlim([min(data)-5, max(data)+5])

plt.hist(data, bins=bins, alpha=0.5)
plt.title('Iowa Obamacare Prices for 2017')
plt.xlabel('Grouped in $20 bins')

plt.ylabel('Count')
#fig, ax = plt.subplots()
#ax.xaxis.set_major_formatter(formatter)



plt.savefig('IowaACA.png')
