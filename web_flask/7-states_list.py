#!/usr/bin/pyrhon3
"""
7--states_list module
"""
from flask import Flask
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def close_session():
    """Removes the current SQLAlchemy Session"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Feches list of states"""
    states = storage.all("State")
    return 


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
