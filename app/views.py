from app import app
from app.models.bucketlistApp import BucketlistApp
from .forms import RegistrationForm, LoginForm
from flask import Flask, flash, redirect, render_template, request, session, abort

import os

bucketlistapp = BucketlistApp()


@app.route('/')
@app.route('/index')
@app.route('/login')
def index():
    form = LoginForm()
    if not session.get('logged_in'):
        return render_template('login.html', form=form)


'''@app.route('/')
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
        return "form not validated"'''


@app.route('/')
@app.route('/index')
@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        log_in = bucketlistapp.login(username, password)
        if log_in == "Successfully logged in":
            return render_template('lists.html')
        elif log_in == 'Your username and password combination does not exist, please try again':
            flash(
                'Your username and password combination does not exist, please try again')
            return render_template('login.html')
        elif log_in == 'Your username does not exist':
            return render_template('signup.html')


@app.route('/signup', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm-password']
        sign_up = bucketlistapp.create_user(
            username, password, confirm_password)
        if sign_up == 'Welcome to the Bucketlist app, please login':
            return render_template('login.html')
        elif sign_up == "Your username already exists":
            return render_template('login.html')
        elif sign_up == "Please make sure all the fields are filled in":
            return render_template('signup.html')
    else:
        return render_template('signup.html')


@app.route('/lists')
def bucketlists():
    pass


@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()
