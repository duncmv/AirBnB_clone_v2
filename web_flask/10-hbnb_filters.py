#!/usr/bin/python3
"""creates flask app to handle states an cities"""
from models import *
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def filters():
    """retrieves states"""
    states = storage.all("State")
    amenities = storage.all("Amenity").values()
    return render_template('10-hbnb_filters.html', states=states,
                           amenities=amenities)


@app.teardown_appcontext
def teardown(err):
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
