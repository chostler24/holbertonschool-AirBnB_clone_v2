#!/usr/bin/python3
"""7-states_list.py module"""
from flask import Flask, render_template


app = Flask(__name__)


@app.teardown_appcontext
def teardown(content):
    """teardown that context"""
    import models
    models.storage.close()


@app.route("/states_list", strict_slashes=False)
def state_route():
    """method displays states_list HTML page"""
    import models
    states = models.storage.all(models.state.State)
    return render_template("7-states_list.html", states=states)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
