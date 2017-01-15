import csv
import os
import math
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
            return 1

with open('spd.csv', 'rb') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
	for row in spamreader:
                uri = row[20]
                uri = uri.translate(None, '!@#$')
                stuff = stuff +[max(math.log(num(uri)),1)]
		print uri
                #os.system("curl -i --basic " + uri + " > _"+uri)


#print stuff
data = np.array(stuff) 

# fixed bin size
bins = np.arange(1, math.log(max(data))+0.5, 0.25) # fixed bin size

plt.xlim([0, math.log(max(data))+1])

plt.hist(data, bins=bins, alpha=0.5)
plt.title('Iowa Obamacare Prices for 2017')
plt.xlabel('Grouped in $20 bins')

plt.ylabel('Count')
#fig, ax = plt.subplots()
#ax.xaxis.set_major_formatter(formatter)



plt.savefig('IowaACA.png')
