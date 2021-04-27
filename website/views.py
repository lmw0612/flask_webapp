from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/') # slash route
def home():
    return render_template("home.html")