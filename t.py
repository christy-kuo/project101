#!/usr/bin/python

import json
import pandas as pd
from pandas import DataFrame
import numpy as np
from sqlalchemy import create_engine
import sqlite3
from datetime import datetime

#Connecting to the database 
conn = sqlite3.connect('air_now.sqlite')
#create a Cursor object,allow python to execute command
cursor = conn.cursor()

# create table
cursor.execute('''CREATE TABLE airCurrent
         (AQI INT,
         CategoryName       TEXT,
         CategoryNumber     INT,
         DateObserved       DATE,
         HourObserved       INT,
         Latitude           FLOAT,
         LocalTimeZone      TEXT,
         Longitude         FLOAT,
         ParameterName      TEXT,
         ReportingArea      TEXT,
         StateCode          TEXT,
         DateTimeNow TEXT PRIMARY KEY);''')

#committing changes and closing the connection to the database file
conn.commit()

results = pd.read_sql_query("select * from airCurrent", conn)
print(results)
