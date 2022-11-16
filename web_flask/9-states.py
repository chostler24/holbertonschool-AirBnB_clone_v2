#!/usr/bin/python3
"""9-states.py module"""
from flask import Flask, render_template


app = Flask(__name__)


@app.teardown_appcontext
def teardown(self):
    """tear it down"""
    from models import storage
    storage.close()


@app.route("/states", strict_slashes=False)
def states():
    """displays html page"""


@app.route("/states/<id>", strict_slashes=False)
def states_id():
    """displays html page"""
