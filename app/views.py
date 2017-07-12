from app import app
from flask import Flask, flash, redirect, render_template, request, session, abort
from .forms import RegistrationForm, LoginForm
'''import models'''
import os


@app.route('/')
@app.route('/index')
@app.route('/login')
def index():
    form = LoginForm()
    if not session.get('logged_in'):
        return render_template('login.html', form=form)


@app.route('/')
@app.route('/index')
@app.route('/login', methods=['POST'])
def login():
    form = LoginForm()
    if request.method == 'GET':
        return render_template('login.html', form=form)
    elif request.method == 'POST':
        if form.validate_on_submit():
            # FIXME: Changing from db usage, to check user dictionary
            user = User.query.filter_by(username=form.username.data).first()
            if user:
                if user.password == form.password.data:
                    login_user(user)
                    return "User logged in"
                else:
                    return "Wrong password"
            else:
                return "user doesn't exist"
    else:
        return "form not validated"


@app.route('/signup', methods=['POST', 'GET'])
def register():
    form = RegistrationForm()
    if request.method == 'GET':
        return render_template('signup.html', form=form)


@app.route('/lists')
def bucketlists():
    pass


@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()
