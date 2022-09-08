#!/usr/bin/env python
# coding: utf-8

# In[15]:


import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify
import datetime as dt
from datetime import date, timedelta, datetime

# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite",echo=False)

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)


# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route('/')
def homepage():
    '''List all available routes.'''
    return(
        f"<h1>Wellcome to Hawaii Weather App</h1><br/>"
        f"<h2>Available Routes:</h2><br/>"
        f"&emsp;/api/v1.0/precipitation<br/>"
        f"&emsp;/api/v1.0/stations<br/>"
        f"&emsp;/api/v1.0/tobs<br/>"
        f"<h2>For searching specific time duration:</h2><br/>"
        f"<h6>Input start date in year,month,day after'/' or a duration with 2 dates splited by '/'</h6><br/>"
        f"&emsp;/api/v1.0/<start></<br/>"
        f"&emsp;/api/v1.0/<start>/<end><br/>"
    )    

@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    
    session = Session(engine)

    # Query all date and precipitation
    
    results = session.query(Measurement.prcp).all()
    dates = session.query(Measurement.date).all()
    
    #Convert the query results to a dictionary using `date` as the key and `prcp` as the value.
    
    dic={dates[i][0]:results[i][0] for i in range(0,len(results))}

    session.close()

    # Return the JSON representation of your dictionary.

    return jsonify(dic)

@app.route("/api/v1.0/stations")
def stations():
    
    # Create our session (link) from Python to the DB
    
    session = Session(engine)
 
    # Query all stations
    
    stations = session.query(Station.station).all()
    StationList=[stations[i][0] for i in range(0,len(stations))]
    session.close()

    # Return a JSON list of stations from the dataset
    
    return jsonify(StationList)

@app.route("/api/v1.0/tobs")
def tobs():
    
    # Create our session (link) from Python to the DB
    
    session = Session(engine)
 
    # Query the most active station.
    
    counts=func.count(Measurement.station)
    
    Mostactivity=session.query(Measurement.station).group_by(Measurement.station).order_by(counts.desc()).first()
    
    most_active_station=Mostactivity[0]

    # Query the dates the most active station for the previous year of data
    

    most_recent_date=session.query(Measurement.date).filter(Measurement.station==most_active_station).order_by(Measurement.date.desc()).first()
    
    most_recent_date=dt.datetime.strptime(most_recent_date[0], '%Y-%m-%d').date()
    
    DateYaerAgo=most_recent_date-timedelta(days=365)
    
    # Query the most active station for the previous year of data
    
    Post12M_most_active_station=session.query(Measurement.tobs).filter(Measurement.date>=DateYaerAgo).filter(Measurement.station==most_active_station).all()

    results=[Post12M_most_active_station[i][0] for i in range(0,len(Post12M_most_active_station))]
    
    session.close()

    # Return a JSON list of temperature observations (TOBS) for the previous year.
    
    return jsonify(results)

@app.route("/api/v1.0/<start>")
@app.route("/api/v1.0/<start>/<end>")
def DataBasedOnDate(start=None,end=None):
    """Fetch the data after start date which matchs the path variable supplied by the user, or a 404 if not."""
    
    import re
    
    # Create our session (link) from Python to the DB
    
    session = Session(engine)
 
    # Query 
    
    dates=session.query(Measurement.date).all()
    date_values=[dates[i][0] for i in range(0,len(dates))]
    
    canonicalised1 = re.sub("([^\u0030-\u0039])", '', start)
    if not end:
        #get rid off any symbols and only keep numbers
        
    
        for date in date_values:
            search_term = date.replace('-','')
            
            if search_term == canonicalised1:
                
                result=session.query(func.min(Measurement.tobs),func.avg(Measurement.tobs),func.max(Measurement.tobs)).filter(Measurement.date>=date).all()
                ResultValue=[data for data in result[0]]

                min=f"The minimun temperature after {start} is {round(ResultValue[0],2)} degrees celsius."
                avg=f"The average temperature after {start} is {round(ResultValue[1],2)} degrees celsius."
                max=f"The maximum temperature after {start} is {round(ResultValue[2],2)} degrees celsius."
                output=[min,avg,max]
                
                return jsonify (output)

    canonicalised2 = re.sub("([^\u0030-\u0039])", '', end)    
    for date1 in date_values:
        search_term1 = date1.replace('-','')
        for date2 in date_values:
            search_term2 = date2.replace('-','')
            if search_term1 == canonicalised1 and search_term2 == canonicalised2:
                
                result=session.query(func.min(Measurement.tobs),func.avg(Measurement.tobs),func.max(Measurement.tobs)).filter(Measurement.date>=date1).filter(Measurement.date>=date2).all()
                ResultValue=[data for data in result[0]]

                min=f"The minimun temperature between {start} and {end} is {round(ResultValue[0],2)} degrees celsius."
                avg=f"The average temperature between {start} and {end} is {round(ResultValue[1],2)} degrees celsius."
                max=f"The maximum temperature between {start} and {end} is {round(ResultValue[2],2)} degrees celsius."
                output=[min,avg,max]

                return jsonify (output)            

    session.close()

        # Return a JSON list of stations from the dataset
        
    return jsonify({"error": f"Data between {start} and {end} are not found."}), 404

if __name__ == '__main__':
    app.run(debug=True)






