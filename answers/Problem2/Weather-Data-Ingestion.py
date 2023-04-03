import os
import pandas as pd
import mysql.connector as mysql
import time

#function defination for calculating the timestamp(time required for ingesting the data)
def current_time_stamp():
    query = "SELECT CURRENT_TIMESTAMP"
    cursor = mydb.cursor() #create a cursor to execute querie
    cursor.execute(query)
    time = cursor.fetchall()[0][0]
    return time

#database connection request    
mydb = mysql.connect(host="127.0.0.1", database = 'corteva_challenge_database',user="root", passwd="adina@2295")
#folder path for loading wx-data    
folder_path = "C:\\Data-Import\\wx_data\\"

#The below mentioned fo loop does reads the data from Wx-data using pandas into a csv format and created a dataframe.
for filename in os.listdir(folder_path):
    start_time = current_time_stamp()
    station=filename[:-4]
    weather_data_tmp = pd.read_csv(folder_path +filename, \
    names=['date','max_temperature','min_temperature','precipitation'],\
    index_col=False, delimiter = '\t', header=None)
    weather_data_tmp['Station_id']=station
    weather_data_tmp["id"]= weather_data_tmp['Station_id'].astype(str)+weather_data_tmp["date"].astype(str)
    weather_data_tmp= weather_data_tmp[['id','Station_id','date','max_temperature','min_temperature','precipitation' ]]
    number_records= 0
    cursor= mydb.cursor()
    
#Iterrows helps to optimise the query performance while fetching rows from a table/dataframe.
for i,row in weather_data_tmp.iterrows():
    query = "SELECT * from Weather where id=(%s)"
    cursor.execute(query,(row[0],))
    
    if cursor.fetchall()==[]:
       query = "INSERT INTO Corteva_Challenge_Database.Weather VALUES (%s,%s,%s,%s,%s,%s)"
       cursor.execute(query, tuple(row))
       number_records+=1

    if number_records!=0:
        end_time = current_time_stamp()
        query = "INSERT INTO Corteva_Challenge_Database.Logs VALUES (%s,%s,%s,%s)" 
        cursor.execute(query, ("Weather_"+filename, start_time, end_time,number_records))
#to commit the final state of the database for reflection of the data stored in the database.    
mydb.commit()
