import numpy as np

import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from collections import defaultdict

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine,reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station
# 2. Create an app, being sure to pass __name__
app = Flask(__name__)


# index route
@app.route("/")
def home():
    print("Server received request for 'Home' page...")
    return (
        f"Welcome to the Hawaii Weather Check</br>"
        f"Options include the following;</br>"
        f"/api/v1.0/precipitation</br>"
        f"/api/v1.0/stations</br>"
        f"/api/v1.0/tobs</br>"
        f"/api/v1.0/start date</br>"
        f"/api/v1.0/start date/end date</br>"
        f"Please format all start and end dates Y-M-D"
    )


# Return the JSON representation of your precipitation dictionary.
@app.route("/api/v1.0/precipitation")
def precipitation():
    print("Server received request for 'Precipitation' page...")
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all precipitation records per date """
    # Query all dates and precipitation records
    results = session.query(Measurement.date,Measurement.prcp).all()

    session.close()

    # Convert list of tuples into dictionary with date as key to precipitation values
    prcp_dict = defaultdict(list)
    for i,j in results:
        prcp_dict[i].append(j)

    return jsonify(prcp_dict)

# station information requested
@app.route("/api/v1.0/stations")
def stations():
    print("Server received request for 'Station' page...")
    session = Session(engine)

    """Return a list of all station names"""
    # Query all station names
    results = session.query(Station.name).all()


    session.close()

    # Convert into normal list
    all_names = list(np.ravel(results))

    return jsonify(all_names)
# temperature information requested
@app.route("/api/v1.0/tobs")
def tobs():
    print("Server received request for 'tobs' page...")
    session = Session(engine)

    """Return a list of all temperatures for past year for the most active station"""
    # Query all temperatures within past year for selected station
    last_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    year_ago = dt.datetime.strptime(last_date[0],"%Y-%m-%d") - dt.timedelta(days=365)
    one_station_results = session.query(Measurement.date,Measurement.tobs).\
    group_by(Measurement.date).\
    filter(Measurement.date > year_ago).\
    filter_by(station = 'USC00519281').\
    order_by(Measurement.date).all()

    session.close()

    # Convert list of tuples into normal list
    results = list(np.ravel(one_station_results))

    return jsonify(results)
# only start date provided
@app.route("/api/v1.0/<start>")
def start(start):
    print("Server received request for 'start' page...")
    session = Session(engine)

    """Return min, average, and max temps from start date"""
    # Query min, average, and max temps from start date
    query_result = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
    filter(Measurement.date > start).all()


    session.close()

    # Convert list of tuples into normal list
    results = list(np.ravel(query_result))

    return jsonify(results)




# start and end date provided
@app.route("/api/v1.0/<start>/<end>")
def startend(start,end):
    print("Server received request for 'About' page...")
    session = Session(engine)

    """Return min, average, and max temps between start and end dates"""
    # Query min, average, and max temps from start date to end date
    query_result = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
    filter(Measurement.date > start).filter(Measurement.date < end).all()


    session.close()

    # Convert list of tuples into normal list
    results = list(np.ravel(query_result))

    return jsonify(results)



if __name__ == "__main__":
    app.run(debug=True)
