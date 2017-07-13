from app import app
from app.models.users import User
from app.models.bucketlistApp import BucketlistApp
'''from .forms import RegistrationForm, LoginForm'''
from flask import Flask, flash, redirect, render_template, request, session, abort

import os

bucketlistapp = BucketlistApp()
username = ''


@app.route('/')
@app.route('/index')
@app.route('/login')
def index():
    if not session.get('logged_in'):
        return render_template('login.html')


@app.route('/')
@app.route('/index')
@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        global username
        username = request.form['username']
        password = request.form['password']
        log_in = bucketlistapp.login(username, password)
        if log_in == "Successfully logged in":
            return render_template('lists.html')
        elif log_in == "Your username and password combination is wrong, please try again":
            flash(
                "Your username and password combination is wrong, please try again")
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


@app.route('/lists', methods=['POST', 'GET'])
def bucketlists():
    if request.method == 'POST':
        checkbox = request.form.get['checkbox']
        list_name = request.form['list_name']
        details = request.form['description']
        button = request.form['add list']
        # TODO: Figure out how to pick up currently logged in username
        if checkbox and button:
            global username
            new_list = User(username)
            new_list.create_list(list_name, details)
            return render_template('lists.html')
        else:
            flash('Make sure your input is limited to words')


@app.route("/logout")
def logout():
    pass
    # TODO: implement
    '''session['logged_in'] = False
    return home()'''
