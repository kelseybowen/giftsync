from flask_app import app
from flask import render_template, request, redirect, session, flash
from flask_app.models import user
# from flask_app.controllers import sightings_controller
# from flask_bcrypt import Bcrypt
# bcrypt = Bcrypt(app)


@app.route('/')
def index():
    return render_template("index.html")