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

df = pd.read_csv('testdata.csv')
json_dict = {}

for date_range, flights in df.groupby('DateDpt--DateAr'):
    flights_no_date = flights.drop('DateDpt--DateAr', axis=1)
    json_dict[date_range]= map(list, flights_no_date.values)
    
with open('testdata.json', 'w') as f:
     json.dump(json_dict, f, indent=4, sort_keys=True)

