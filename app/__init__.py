from flask import Flask

'''
Initialising Flask app
'''
app = Flask(__name__)

'''
Loading the configuration file
'''
app.config.from_object('config')
app.config['SESSION_TYPE'] = 'filesystem'

from app import views
