"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from flaskdemoproject2 import app
from flask_wtf import FlaskForm
from wtfform import StringFeild, SubmitFeild    
from wtfform.validators import DataRequired
import pandas as pd
import Matplotlib as plt

class CountryForm (FlaskForm) :
    name=StringStringFeild('Country name?)' , validators =[DataRequrired()])
    submit = SubmitFeild('Submit')

app.config['SECRET_KEY']='The first argument to the field'

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/photos')
def photos():
    """Renders the home page."""
    return render_template(
        'photos.html',
        title='My Photos',
        message='Your application description page.'
    )
@app.route('/query')
def Query():
    """Renders the home page."""
    return render_template(
        'Query.html',
        year=datetime.now().year,
        title='Using Web Forms (Query)',
        message='This page demonstrae how to use web forms.'
    )

@app.route('/query', methdods= ['GET', 'POST'])
def Query():
       print 
       return render_template(
       'Query.html',
        year=datetime.now().year,
        title='Using Web Forms (Query)',
        message='This page demonstrae how to use web forms.'
    )


