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

@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """displays HBNB"""
    return 'C {}'.format(str(text).replace("_", " "))

@app.route('/python', strict_slashes=False, defaults={'text':'is cool'})
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    """displays HBNB"""
    return 'Python {}'.format(str(text).replace("_", " "))

@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """displays HBNB"""
    return '{:d} is a number'.format(n)


if __name__ == '__main__':
   """Starting the app"""
   app.run(host='0.0.0.0', port='5000')
