import os
import pandas as pd
import mysql.connector as mysql
import time

def current_time_stamp():
    
    query = "SELECT CURRENT_TIMESTAMP"
    
    cursor = mydb.cursor() #create a cursor to execute queries
    cursor.execute(query)
    time = cursor.fetchall()[0][0]
    return time
    
mydb = mysql.connect(host="127.0.0.1", database = 'corteva_challenge_database',user="root", passwd="adina@2295")
folder_path = "C:\\Data-Import\\yld_data\\"
corn_yield_data = pd.read_csv(folder_path + 'US_corn_grain_yield.txt', names=['year','corn_yield'],\
                      index_col=False, delimiter = '\t', header=None)

num_records=0
# creating column list for insertion 
cols = "','".join([str(i) for i in corn_yield_data.columns.tolist()])

for i,row in corn_yield_data.iterrows():
    start_time = current_time_stamp()
    query = "SELECT * FROM Yield where year=%s"

    cursor = mydb.cursor() #create a cursor to execute queries
    cursor.execute(query, (int(row[0]),))

    if cursor.fetchall()==[]:

        sql = "INSERT INTO Corteva_Challenge_Database.Yield VALUES (%s,%s)"
        cursor.execute(sql, tuple(row)) 
        num_records+=1
    
if num_records!=0:       
    end_time = current_time_stamp()

    query = "INSERT INTO Corteva_Challenge_Database.Logs VALUES (%s,%s,%s,%s)" 
    cursor.execute(query, ("US_corn_grain_yield_data.txt", start_time, end_time,num_records)) 

mydb.commit()    
#30 rows inserted.


    
