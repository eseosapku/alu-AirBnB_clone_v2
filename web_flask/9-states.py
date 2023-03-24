#!/usr/bin/python3
""" starts a Flask web application """
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states_list():
    """
    returns a HTML page
    """
    return render_template('7-states_list.html',
                           states=storage.all('State').values())


@app.route('/states/<id>', strict_slashes=False)
def states_id(id):
    """
    return a HTML page
    """
    state_list = storage.all('State').values()
    for state in state_list:
        if state.id == id:
            return render_template('9-states.html', state=state)
    return render_template('9-states.html', state=None)


@app.teardown_appcontext
def teardown(self):
    """
    closes the session
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
