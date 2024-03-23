#!/usr/bin/python3
"""creates flask app to handle states an cities"""
from models import *
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """retrieves data for page"""
    states = storage.all("State")
    amenities = storage.all("Amenity").values()
    places = storage.all("Place").values()
    users = storage.all("User").values()
    return render_template('100-hbnb.html', states=states,
                           amenities=amenities, places=places,
                           users=users)


@app.teardown_appcontext
def teardown(err):
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0')
