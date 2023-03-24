#!/usr/bin/python3
"""
starts a Flask web application 
"""
from models import storage
from models.amenity import Amenity
from models.state import State
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def filters_list():
    """
    returns a HTML page
    """
    states = storage.all('State').values()
    amenities = storage.all('Amenity').values()
    return render_template(
        "10-hbnb_filters.html",
        states=states, amenities=amenities)


@app.teardown_appcontext
def teardown(self):
    """
    Comment
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
