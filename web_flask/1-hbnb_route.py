#!/usr/bin/python3
"""
0-hello_route module
Starts a Flask web application
"""
from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def root():
    """The root of the app"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """displays HBNB"""
    return 'HBNB'


if __name__ == '__main__':
   """Starting the app"""
   app.run(host='0.0.0.0', port='5000')
