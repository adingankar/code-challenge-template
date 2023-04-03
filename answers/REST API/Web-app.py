from flask import Flask, request, jsonify
import sqlite3
from pathlib import Path

app = Flask(__name__)

# Connect to the database
mydb = mysql.connect(host="127.0.0.1", database = 'corteva_challenge_database',user="root", passwd="adina@2295")
cur = mydb.cursor()

@app.route("/")
def hello():
    # just as a reference for testing the end points with different params
    s0 = "http://127.0.0.1:5000/api/weather"
    s1 = "http://127.0.0.1:5000/api/weather/stats"
    mylink = create_link(s0)
    mylink += create_link(s1)
    return "Hello!\n" + "\n testing urls: \n" + mylink + "\n"

#for weather:
@app.route("/api/weather")
def weather_data():
    # Extract query parameters
    station_id = "USC00110072"
    date = "1985-01-01"
    page = 1
    per_page = 5
    station_id = request.args.get("station_id")
    date = request.args.get("record_date")
    page = int(request.args.get("page", 1))
    per_page = int(request.args.get("per_page", 10))

 #Building a query:
    query = "SELECT Station_ID, Record_Date, Min_Temp, Max_Temp, Precipitation FROM weather_data"
    where_clauses = []
    if station_id:
        where_clauses.append(f"Station_ID = '{station_id}'")
    if date:
        where_clauses.append(f"Record_Date = '{date}'")
    if where_clauses:
        query += " WHERE " + " AND ".join(where_clauses)

 # Paginating the results
    query += f" LIMIT {per_page} OFFSET {(page - 1) * per_page}"

    # Execute the query and fetch the results
    cur.execute(query)
    results = cur.fetchall()

 # Formatting the results as a JSON response.
    response = {
        "data": [
            {
                "Station_ID": result[0],
                "Record_Date": str(result[1]),
                "Min_Temp": result[2],
                "Max_Temp": result[3],
                "Precipitation": result[4],
            }
            for result in results
        ]
    }
    return response

#for weather stats:
@app.route("/api/weather/stats")
def weather_stats():
    # Extract query parameters
    station_id = request.args.get("station_id")
    year = request.args.get("record_year")
    # Build the query
    query = "SELECT * FROM weather_stats"
    where_clauses = []
    if station_id:
        where_clauses.append(f"Station_ID = '{station_id}'")
    if year:
        where_clauses.append(f"Record_Year = {year}")
    if where_clauses:
        query += " WHERE " + " AND ".join(where_clauses)

    # return jsonify(query)

# Building the query
    cur.execute(query)
    results = cur.fetchall()

# Format the results for json response.
    response = {
        "data": [
            {
                "Station_ID": result[0],
                "Record_Year": result[1],
                "Avg_MinTemp": round(result[2], 1),
                "Avg_MaxTemp": round(result[3], 1),
                "Total_Precipitation": round(result[4], 1),
            }
            for result in results
        ]
    }
    return response
  
# helper method to create the string link into hyperlink in html
def create_link(link1):
    homeeurl = "<div>"
    homeeurl += "<a href=\""
    homeeurl += link1
    homeeurl += "\" > " + link1 + "</a>"
    homeeurl += "</div>"
    return homeeurl

if __name__ == "__main__":
    app.run(debug=True)
