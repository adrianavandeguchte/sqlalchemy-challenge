import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

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
        f"/api/v1.0/<start></br>"
        f"/api/v1.0/<start>/<end></br>"
    )

# precipitation information requested
Convert the query results to a dictionary using date as the key and prcp as the value.

Return the JSON representation of your dictionary.
@app.route("/api/v1.0/precipitation")
def about():
    print("Server received request for 'precipitation' page...")
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all passenger names"""
    # Query all passengers
    results = session.query(Measurement.date,Measurement.prcp).all()

    session.close()

    # Convert list of tuples into normal list
    prcp_dict = dict(np.ravel(results))

    return jsonify(prcp_dict)

# station information requested
@app.route("/api/v1.0/stations")
def about():
    print("Server received request for 'About' page...")
    return "Welcome to my 'About' page!"
# temperature information requested
@app.route("/api/v1.0/tobs")
def about():
    print("Server received request for 'About' page...")
    return "Welcome to my 'About' page!"
# only start date provided
@app.route("/api/v1.0/<start>")
def about():
    print("Server received request for 'About' page...")
    return "Welcome to my 'About' page!"
# start and end date provided
@app.route("/api/v1.0/<start>/<end>")
def about():
    print("Server received request for 'About' page...")
    return "Welcome to my 'About' page!"



if __name__ == "__main__":
    app.run(debug=True)
