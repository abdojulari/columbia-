
import pandas as pd
import datetime
from pandas_datareader import data, wb
import csv
import json
#declaring libraries for the analysis 
out= open("testfile.csv", "rb") # read the .csv file
data = csv.reader(out)
data = [[row[0],row[1] + "_" + row[2],row[3] +"_" + row[4], row[5] + "--" + row[6]] for row in data] 
#this part is mainly to concatenate the City and country
out.close() 

out=open("testdata.csv", "wb")
output = csv.writer(out)
for row in data:
    output.writerow(row)
out.close()

import csv, json


csvfile = open('testdata.csv', 'rU')
jsonfile = open('testdata.json', 'w')

reader = csv.DictReader(csvfile,)

for row in reader:
   json.dump({ row['DateDpt--DateAr'] : (row['AuthorID'], row['ArCity_ArCountry'], row['DptCity_DptCountry']) }, jsonfile, indent=4)
   jsonfile.write(',\n')

