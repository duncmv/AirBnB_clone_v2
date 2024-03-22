#!/usr/bin/python3
"""retrieves states and returns html template"""
from flask import Flask, render_template
from models import storage
from models.state import State
import operator
app = Flask(__name__)



@app.route('/states_list', strict_slashes=False)
def states():
    """retrieve states"""
    states= storage.all('State')
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown(err):
    """close session"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0')