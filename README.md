# Code Challenge Template
This repository contains my solution to the challenge posed by Corteva. In this exercise, a dataset containing weather and crop yield data. In this exercise, I designed a database for maintaining these two datasets in two tables- Weather and Yield data. By using the weather data as source I designed another table Weather_stats that contains the statstics of weather for each year and each station ID.

About Data
Weather Data Description
The wx_data directory Link has files containing weather data records from 1985-01-01 to 2014-12-31. Each file corresponds to a particular weather station from Nebraska, Iowa, Illinois, Indiana, or Ohio.

Each line in the file contains 4 records separated by tabs:

The date (YYYYMMDD format)
The maximum temperature for that day (in tenths of a degree Celsius)
The minimum temperature for that day (in tenths of a degree Celsius)
The amount of precipitation for that day (in tenths of a millimeter)
Missing values are indicated by the value -9999.

Yield Data Description
The yld_data directory Link has files containing yield data record from 1985 to 2014.

Each line in the file contains 2 records separated by tabs:

Year (YYYYMMDD format)
Yield
![image](https://user-images.githubusercontent.com/78924701/229616490-b70bd546-5177-41ac-931a-aa668e3d9eb5.png)


Approach of execution : 
Created databases : weather, yeild , statistics and logs for each of the records respectively.
Created a seperate script for data ingestion which loads the txt records from wx_data and yx_data folder to the weather and yeild databases.
Created a flask api which unit tests to be validated since the data did had a check for duplicate records and does not contain invalid parameters, so unit test are calculated on the factors of empty strings passed to the json.
Containerized the flask application by using docker container.

