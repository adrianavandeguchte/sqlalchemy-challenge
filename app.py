# 1. import Flask
from flask import Flask

# 2. Create an app, being sure to pass __name__
app = Flask(__name__)


# index route
@app.route("/")
def home():
    print("Server received request for 'Home' page...")
    return "Welcome to my 'Home' page!"

# precipitation information requested
@app.route("/api/v1.0/precipitation")
def about():
    print("Server received request for 'About' page...")
    return "Welcome to my 'About' page!"
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
