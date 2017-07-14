from app import app
from app.models.users import User
from app.models.bucketlistApp import BucketlistApp
from flask import Flask, flash, redirect, render_template, request, session, url_for

import os

bucketlistapp = BucketlistApp()
logged_in = []


@app.route('/')
@app.route('/login')
def home():
    '''
    This function loads the login.html page.

    '''
    if not session.get('logged_in'):
        return render_template('login.html')


@app.route('/')
@app.route('/login', methods=['POST'])
def login():
    '''
    Logs in the pre-existing users 
    when their username and password combination
    matches.
    '''
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        log_in = bucketlistapp.login(username, password)

        if log_in == "Successfully logged in":
            session['username'] = request.form['username']
            flash('You have succesfully logged in')

            return render_template('lists.html')
        elif log_in == "Your username and password combination is wrong, please try again":
            flash(
                "Your username and password combination is wrong, please try again")
            return render_template('login.html')
        elif log_in == 'Your username does not exist':
            flash('Your username does not exist')
            return render_template('signup.html')
    else:
        return render_template('login.html', logged_in=username)


@app.route('/signup', methods=['POST', 'GET'])
def register():
    '''
    Creates and stores the users credentials in 
    the usercredentials dictionary when the username, password 
    and verification password match
    '''
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm-password']
        sign_up = bucketlistapp.create_user(
            username, password, confirm_password)
        if sign_up == 'Welcome to the Bucketlist app, please login':
            flash('Welcome to the Bucketlist app, please login')
            return render_template('login.html')
        elif sign_up == "Your username already exists":
            flash("Your username already exists")
            return render_template('login.html')
        elif sign_up == "Please make sure all the fields are filled in":
            flash("Please make sure all the fields are filled in")
            return render_template('signup.html')
    else:
        return render_template('signup.html')


@app.route('/lists', methods=['POST', 'GET'])
def create_bucketlist():
    '''
    create_bucketlist creates bucketlists and displays them on and refreshes
    the page.
    '''
    currentuser = bucketlistapp.check_for_user(session['username'])
    if not currentuser:
        redirect(url_for('login'))

    if request.method == 'POST':
        list_name = request.form['list_name']
        details = request.form['description']
        '''current_user = bucketlistapp.users[currentuser]'''
        currentuser.create_list(list_name, details)
        your_bucketlists = currentuser.display_list()
        print(your_bucketlists)
        return render_template('lists.html', userbuckets=your_bucketlists)
    else:
        return 'did not work'


@app.route('/lists', methods=['GET'])
def view_bucketlists(list_name):
    '''
    To display the bucketlists
    '''
    currentuser = bucketlistapp.check_for_user(session['username'])

    if not currentuser:
        redirect(url_for('login'))

    if request.method == 'GET':
        currentuser.view_list(list_name)
        return render_template('items.html')
    else:
        return 'The list name does not exist'


@app.route('/items', methods=['POST', 'GET'])
def create_items():
    '''
    creates items and displays them on and refreshes
    the page.
    '''
    currentuser = bucketlistapp.check_for_user(session['username'])
    if not currentuser:
        redirect(url_for('login'))

    if request.method == 'POST':
        item_name = request.form['item_name']
        details = request.form['description']
        currentuser.create_item(item_name, details)
        your_bucketlists = currentuser.display_list()
        print(your_bucketlists)
        return render_template('lists.html', userbuckets=your_bucketlists)
    else:
        return 'did not work'


@app.route("/logout")
def logout():
    '''
    This function logs out the current user
    '''
    # TODO: implement
    return render_template('login.html')
