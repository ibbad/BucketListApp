import json
from . import main
from .. import db
from ..models import User
from flask import render_template, request


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/signupform')
def show_signup():
    return render_template('signup.html')


@main.route('/signup', methods=['POST', 'GET'])
def signup():
    # Read form values from incoming request
    _name = request.form['inputName']
    _email = request.form['inputEmail']
    _password = request.form['inputPassword']

    # validate values
    if _name and _email and _password:
        if User.query.filter_by(email=_email).first() is not None:
            return json.dumps(
                {'error': '<span>User already registered.<span>'})
        # add user to database.
        user = User(name=_name, email=_email, password=_password)
        db.session.add(user)
        db.session.commit()
        return json.dumps(
            {'html': '<span>User successfully registered.<span>'})
    else:
        return json.dumps({'html': '<span>Enter required inputs.</span>'})
