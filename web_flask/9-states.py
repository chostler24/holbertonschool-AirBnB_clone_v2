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
def states_route():
    """displays html page"""
    from models import storage
    from models.state import State
    state_list = storage.all(State)
    return render_template("9-states.html", state_list=state_list)


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """displays html page"""
    from models import storage
    from models.state import State
    states = storage.all(State)
    state_list = None
    for state in states.values():
        if state.id == id:
            state_list = state
    return render_template("9-states.html", state_list=state_list)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
