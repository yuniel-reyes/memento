from flask import render_template, session, redirect, url_for, flash, current_app
from . import main

""" Index """
@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')