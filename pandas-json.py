# In The Same Boats:
# Converter using Pandas

import pandas as pd
import pandas_datareader
from datetime import date, timedelta as td, datetime
import numpy as np
import json

df = pd.read_csv('testfile.csv')
df["ArCiCo"] = df["ArCity"] + "_" + df["ArCountry"]
df["DptCiCo"] = df["DptCity"] + "_" + df["DptCountry"]
df["Date"] = df["DateAr"] 
df.DateDpt = pd.to_datetime(df.DateDpt)
df.DateAr = pd.to_datetime(df.DateAr)
# df = df.set_index('DateAr')
df = pd.DataFrame(df, columns = ['AuthorID', 'ArCiCo', 'DptCiCo', 'Date'])

#print (df)
#df.to_csv('pandas-csv.csv')
#df = pd.read_csv('pandas-csv.csv')
json_dict = {}

for date_range, flights in df.groupby('Date'):
    flights_no_date = flights.drop('Date', axis=1)
    json_dict[date_range]= map(list, flights_no_date.values)
    
with open('testdata.json', 'w') as f:
     json.dump(json_dict, f, indent=4, sort_keys=True)






