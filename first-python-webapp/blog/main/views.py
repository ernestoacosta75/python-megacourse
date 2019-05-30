'''
This file will contains all the views that will be exported
by our module.
'''
from flask import render_template

from . import main


@main.route('/')
def index():
    return render_template('main/index.html')