#!/usr/bin/python3
"""starts a Flask web application"""
from flask import Flask, abort, render_template
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """returns simple greeting"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """returns HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """c route"""
    new_text = text.replace("_", " ")
    return "C {}".format(new_text)


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """python route"""
    new_text = text.replace("_", " ")
    return "Python {}".format(new_text)


@app.route("/number/<n>", strict_slashes=False)
def number(n):
    try:
        n = int(n)
        return "{} is a number".format(n)
    except Exception:
        abort(404)


@app.route("/number_template/<n>", strict_slashes=False)
def number_template(n):
    try:
        n = int(n)
        return render_template('5-number.html', n=n)
    except Exception:
        abort(404)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
