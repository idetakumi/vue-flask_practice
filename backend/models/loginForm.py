from flask_wtf import FlaskForm
from wtforms import TextField, PasswordField, validators, SubmitField

class LoginForm(FlaskForm):
    userName = TextField('userName', validators=[validators.Required()])
    password = PasswordField('Password', validators=[validators.Required()])
    submit = SubmitField('ログイン')


