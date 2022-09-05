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
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f'For searching specific time duration:<br/>'
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end><br/>"
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
    

    most_recent_date=session.query(Measurement.date).filter(Measurement.station==most_active_station).        order_by(Measurement.date.desc()).first()
    
    most_recent_date=dt.datetime.strptime(most_recent_date[0], '%Y-%m-%d').date()
    
    DateYaerAgo=most_recent_date-timedelta(days=365)
    
    # Query the most active station for the previous year of data
    
    Post12M_most_active_station=session.query(Measurement.tobs).        filter(Measurement.date>=DateYaerAgo).filter(Measurement.station==most_active_station).all()

    results=[Post12M_most_active_station[i][0] for i in range(0,len(Post12M_most_active_station))]
    
    session.close()

    # Return a JSON list of temperature observations (TOBS) for the previous year.
    
    return jsonify(results)

@app.route("/api/v1.0/<start>")

def DataAfterStartDate(start):
    """Fetch the data after start date which matchs the path variable supplied by the user, or a 404 if not."""
    import re
    
    # Create our session (link) from Python to the DB
    
    session = Session(engine)
 
    # Query 
    canonicalised = re.sub("([^\u0030-\u0039])", '', start)
    
    dates=session.query(Measurement.date).all()
    date_values=[dates[i][0] for i in range(0,len(dates))]

    for date in date_values:
        search_term = date.replace('-','')
        
        if search_term == canonicalised:
            
            TMIN=session.query(func.min(Measurement.tobs)).filter(Measurement.date>=date)
            minT=round(TMIN[0][0],2)
            TAVG=session.query(func.avg(Measurement.tobs)).filter(Measurement.date>=date)
            avgT=round(TAVG[0][0],2)
            TMAX=session.query(func.max(Measurement.tobs)).filter(Measurement.date>=date)
            maxT=round(TMAX[0][0],2)
            
            min=f"The minimun temperature between {start} is {minT} degrees celsius."
            avg=f"The average temperature between {start} is {avgT} degrees celsius."
            max=f"The maximum temperature between {start} is {maxT} degrees celsius."
            result=[min,avg,max]

            return jsonify (result)
            
    

    session.close()

    # Return a JSON list of stations from the dataset
    
    return jsonify({"error": f"Data with {start} not found."}), 404

@app.route("/api/v1.0/<start>/<end>")

def DataBetweenDates(start,end):
    """Fetch the data between start date and end date which match the path variable supplied by the user, or a 404 if not."""
    import re
    
    # Create our session (link) from Python to the DB
    
    session = Session(engine)
 
    # Query 
    canonicalised1= re.sub("([^\u0030-\u0039])", '', start)
    canonicalised2= re.sub("([^\u0030-\u0039])", '', end)

    dates=session.query(Measurement.date).all()
    date_values=[dates[i][0] for i in range(0,len(dates))]

    for date1 in date_values:
        search_term1 = date1.replace('-','')
        for date2 in date_values:
            search_term2 = date2.replace('-','')
            if search_term1 == canonicalised1 and search_term2 == canonicalised2:
                
                TMIN=session.query(func.min(Measurement.tobs)).filter(Measurement.date>=date1).filter(Measurement.date>=date2)
                minT=round(TMIN[0][0],2)
                TAVG=session.query(func.avg(Measurement.tobs)).filter(Measurement.date>=date1).filter(Measurement.date>=date2)
                avgT=round(TAVG[0][0],2)
                TMAX=session.query(func.max(Measurement.tobs)).filter(Measurement.date>=date1).filter(Measurement.date>=date2)
                maxT=round(TMAX[0][0],2)
                
                min=f"The minimun temperature between {start} and {end} is {minT} degrees celsius."
                avg=f"The average temperature between {start} and {end} is {avgT} degrees celsius."
                max=f"The maximum temperature between {start} and {end} is {maxT} degrees celsius."
                result=[min,avg,max]

                return jsonify (result)

    session.close()

    # Return a JSON list of stations from the dataset
    
    return jsonify({"error": f"Data with {start} not found."}), 404




if __name__ == '__main__':
    app.run(debug=True)


# In[ ]:




