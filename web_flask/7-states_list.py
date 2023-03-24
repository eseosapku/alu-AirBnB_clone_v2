#!/usr/bin/python3
""" starts a Flask web application """
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """
    returns a HTML page with a list of states
    """
    return render_template('7-states_list.html',
                           states=storage.all('State').values())

@app.teardown_appcontext
def close_session(self):
    """
    End session after request 
    """
    storage.close()
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
