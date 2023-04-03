import mysql.connector as mysql

#Creating the Weather Data Table:
try:
    mydb = mysql.connect(host="127.0.0.1", database = 'corteva_challenge_database',user="root", passwd="adina@2295")
    # check if the connection is established
    print(mydb.is_connected())
    #Created a primary key to make the computation easier id= Stationid+date
    query = "CREATE TABLE Weather( id VARCHAR(30) NOT NULL, Stationid VARCHAR(20) ,date DATE, \
            max_temperature INT(10), min_temperature INT(10),precipitation INT(10), \
            PRIMARY KEY (id))"
    cursor = mydb.cursor() #create a cursor to execute queries
    cursor.execute(query)
    print("Weather Table Created!!")
    mydb.close()
except Exception as e:
    mydb.close()
    print(str(e))

#Creating the Yeild Table :
try:
    mydb = mysql.connect(host="127.0.0.1", database = 'corteva_challenge_database',user="root", passwd="adina@2295")
    # check if the connection is established
    print(mydb.is_connected())
    query = "CREATE TABLE Yield(year INT NOT NULL,corn_yield INT(10), PRIMARY KEY (year))"
    cursor = mydb.cursor() 
    cursor.execute(query)
    print("Yeild Table Created!!")
    mydb.close()
except Exception as e:
    mydb.close()
    print(str(e))   

#Creating the Logs Data Table:

try:
    mydb = mysql.connect(host="127.0.0.1", database = 'corteva_challenge_database',user="root", passwd="adina@2295")
    # check if the connection is established
    print(mydb.is_connected())
    query = "CREATE TABLE Logs(File VARCHAR(30), start_time TIMESTAMP, end_time TIMESTAMP,\
    num_records INT(20))"
    cursor = mydb.cursor() 
    cursor.execute(query)
    print("Logs Table Created!!")
    mydb.close()
except Exception as e:
    mydb.close()
    print(str(e))    

try:
    mydb = mysql.connect(host="127.0.0.1", database = 'corteva_challenge_database',user="root", passwd="adina@2295")
    # check if the connection is established
    print(mydb.is_connected())
    query = "CREATE TABLE Stastistics(year INT(4), Stationid VARCHAR(20), Average_maximum_temperature DECIMAL(20,2),\
    Average_minimum_temperature DECIMAL(20,2), Total_accumulated_precipitation DECIMAL(20,2))"
    cursor = mydb.cursor() 
    cursor.execute(query)
    print("Statistics Table Created!!")
    mydb.close()
except Exception as e:
    mydb.close()
    print(str(e))    
