#!/usr/bin/python3
"""
script that starts a Flask web application
"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    # """ returns hello HBNB """
    return "Hello HBNB!"

if __name__ == "__main__":
    # """ everything starts here """
    app.run(host="0.0.0.0", port=5000, debug=True)
