from flask import render_template, url_for
from budget_flask import app
from budget_flask.forms import *
from budget_flask.models import *

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/test')
def test():
    return render_template('test.html')
