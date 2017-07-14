from flask import Flask

app = Flask(__name__)
app.config.from_object('config')
app.config['SESSION_TYPE'] = 'filesystem'

from app import views
