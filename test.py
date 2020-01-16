#!/usr/bin/python

import json
import requests
import pandas as pd
from pandas.io.json import json_normalize
from pandas import DataFrame
import numpy as np
from sqlalchemy import create_engine
import sqlite3
from datetime import datetime

#API parameters
options = {}
options["url"] = "http://www.airnowapi.org/aq/observation/zipCode/current/"
options["format"] = "application/json"
options["zipCode"] = "94607"
options["distance"] = "25"
options["api_key"] = "FFA4EF59-2AA7-4E71-9934-556C3EE870D7"


# API request URL
REQUEST_URL_current = options["url"] \
               + "?format=" + options["format"] \
                  + "&zipCode=" + options["zipCode"] \
                  + "&distance=" + options["distance"] \
                  + "&API_KEY=" + options["api_key"]

response = requests.get(REQUEST_URL_current)
data = json.loads(response.text)
df = json_normalize(data[1])
Products_list = df.values.tolist()
val = Products_list[0]
val.append(datetime.now())



#Connecting to the database 
conn = sqlite3.connect('air_now.sqlite')
#create a Cursor object,allow python to execute command
cursor = conn.cursor()


# insert value from api into table 
sql = 'INSERT INTO airCurrent (AQI,CategoryName,CategoryNumber,DateObserved,HourObserved,Latitude,LocalTimeZone,Longitude,ParameterName,ReportingArea,StateCode,DateTimeNow) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)'

cursor.execute(sql,val)

conn.commit()
#conn.close()

results = pd.read_sql_query("select * from airCurrent", conn)
print(results)
