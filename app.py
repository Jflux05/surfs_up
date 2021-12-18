# Import the Dependencies: import is datetime, NumPy, and Pandas. and add 
# the dependencies we need for SQLAlchemy, which will help us access our data in the SQLite database. 

import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# Finally, add the code to import the dependencies that we need for Flask.
from flask import Flask, jsonify

# Set Up the Database
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect the database into our classes
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

# create a variable for each of the classes so that we can reference them later
Measurement = Base.classes.measurement
Station = Base.classes.station

# create a session link from Python to our database
session = Session(engine)

# Create a New Flask App Instance... define our Flask app
app = Flask(__name__)

# Create Flask Routes
# define the welcome route 
@app.route('/')

# create a function welcome() with a return statement. add the precipitation, stations, tobs, and temp routes 
# that we'll need for this module into our return statement. We'll use f-strings to display them for our investors:

def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end/
    ''')

# Create the route for the precipitation analysis
@app.route("/api/v1.0/precipitation")

# Create the precipitation() function: and make sure that it that calculates the date one year ago from the most recent date 
# in the database. 
# write a query to get the date and precipitation for the previous year.
# Finally, we'll create a dictionary with the date as the key and the precipitation as the value.
def precipitation():
   prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
   precipitation = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= prev_year).all()
   precip = {date: prcp for date, prcp in precipitation}
   return jsonify(precip) 

# Create the route for the station analysis:
@app.route("/api/v1.0/stations")

# Create the precipitation() function: 
# create a query that will allow us to get all of the stations in our database.
# Next, we will convert our unraveled results into a list. To convert the results to a list, 
# we will need to use the list function, which is list(), and then convert that array into a list. 
# Then we'll jsonify the list and return it as JSON.

def stations():
    results = session.query(Station.station).all()
    stations = list(np.ravel(results))
    return jsonify(stations=stations)


# Create a route for the Monthly Temperature Observations
@app.route("/api/v1.0/tobs")

# Create a function called temp_monthly(): And now, calculate the date one year ago from the last date in the database.
# create a query that will tell us the primary station for all the temperature observations from the previous year.
# Finally, as before, unravel the results into a one-dimensional array and convert that array into a list. 
# Then jsonify the list and return our results
def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).\
      filter(Measurement.station == 'USC00519281').\
      filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)

# Create a route for the Summary Statistics:
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")

# Create a function called stats():
# now create a query to select the minimum, average, and maximum temperatures from our SQLite database. 
# We'll start by just creating a list called sel
# Since we need to determine the starting and ending date, add an if-not statement to our code. 
# # We'll need to query our database using the list that we just made. 
# Then, we'll unravel the results into a one-dimensional array and convert them to a list. 
# Finally, we will jsonify our results and return them.

# Now we need to calculate the temperature minimum, average, and maximum with the start and end dates. 
# We'll use the sel list, which is simply the data points we need to collect. 
# Let's create our next query, which will get our statistics data.

def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps=temps)

    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)
