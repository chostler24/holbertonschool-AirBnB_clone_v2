#!/usr/bin/python3
"""8-cities_by_states.py module"""
from flask import Flask, render_template


app = Flask(__name__)


@app.teardown_appcontext
def teardown(self):
    """teardown that context"""
    from models import storage
    storage.close()


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """displays html page"""
    from models import storage
    from models.state import State
    citys = storage.all(State)
    return render_template("8-cities_by_states.html", citys=citys)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
