#!/usr/bin/python3
"""
7--states_list module
"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def close_session():
    """Removes the current SQLAlchemy Session"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Feches list of states"""
    states = sorted(list(storage.all("State")), key="name")
    return render_template("7-states_list.html", states=state)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
