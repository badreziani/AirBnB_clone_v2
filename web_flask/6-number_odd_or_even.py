#!/usr/bin/python3
"""
0-hello_route module
Starts a Flask web application
"""
from flask import Flask, render_template

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
    """display 'C ', followed by the value of the text variable
    (replace underscore _ symbols with a space )"""

    return 'C {}'.format(str(text).replace("_", " "))


@app.route('/python', strict_slashes=False, defaults={'text': 'is cool'})
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    """display 'Python ', followed by the value of the text variable
    (replace underscore _ symbols with a space )"""
    return 'Python {}'.format(str(text).replace("_", " "))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """display '<n> is a number' only if n is an integer"""
    return '{:d} is a number'.format(n)


@app.route('/number_template/<int:n>')
def number_template(n):
    """Displays a HTML page only if n is an integer
    'Number: <n>'"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even(n):
    """Displays a HTML page only if n is an integer
    'Number: <n> is odd|even'"""
    data = {
        'n':n,
        'odd': 'odd' if n % 2 != 0 else 'even'
    }
    return render_template('6-number_odd_or_even.html', data=data)


if __name__ == '__main__':
    """Starting the app"""
    app.run(host='0.0.0.0', port='5000')
