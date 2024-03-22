#!/usr/bin/python3
"""retrieves states and returns html template"""
from flask import Flask, render_template
from models import storage
from models.state import State
import operator
app = Flask(__name__)



@app.route('/states_list')
def states(states):
    """retrieve states"""
    states = storage.all(State)
    states.sort(key=operator.itemgetter('name'))
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def done():
    """close session"""
    storage.close()