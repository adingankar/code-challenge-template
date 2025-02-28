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


Approach of the project:
I I have created three databases named weather(which will be storing the data from wx_data), yeild(this is used to store the yx_data), statistics(this table is used to store the statistics calculations like the average max temperature, average min temperature & total accumulated precipitation) & logs data which is used to store the 
start and end time commit records for yeild and weather data entries)

II Further more I have created Unit test to validate the results generated from the end-points of restapi.

III I have made use of flask for api configurations and I have created two functions for api/weather and api/weather/stats checkpoint, To containerize which I have used Docker.
