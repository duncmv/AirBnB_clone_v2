#!/usr/bin/python3
"""creates flask app to handle states an cities"""
from models import *
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states():
    """retrieves states"""
    states = storage.all("State")
    return render_template('7-states_list.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def states_given_id(id):
    """retrieves a particular state"""
    states = storage.all("State")
    found_state = None
    for s_id in states:
        if id in s_id:
            found_state = states[s_id]

    return render_template('9-states.html',
                           state=found_state)


@app.teardown_appcontext
def teardown(err):
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0')