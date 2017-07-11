from flask_wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextField, validators
from wtforms.validators import Required, Length, DataRequired


class RegistrationForm(Form):
    username = StringField('Username', [validators.Length(min=4, max=20)])
    password = PasswordField('Password', [
        validators.Required(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField(
        'I accept the Terms of Service and Privacy Notice (updated Jan 22, 2015)', [validators.Required()])


class LoginForm(Form):
    username = StringField('username', [validators.Length(min=4, max=20)])
    password = PasswordField('password', validators=[Required()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log In')
