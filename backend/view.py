from flask import Blueprint, redirect, request, render_template, url_for
from flask_login import login_user, logout_user

from backend import db
from backend.models.user import User
from backend.models.loginForm import LoginForm
from backend.config import BaseConfig

view = Blueprint('app', __name__,
                    static_folder = 'templates',
                    template_folder = 'templates')

@view.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if form.validate_on_submit():
        user, authenticated = User.auth(db.session.query, form.userName.data, form.password.data)
        if authenticated:
            login_user(user, remember=True)
            print('Login successfully.')
            return redirect('/')
        else:
            print('Login failed.')
    return render_template('login.html', form=form, action=url_for('app.login'))

@view.route('/logout', methods=['POST'])
def logout():
    logout_user()
    return redirect('/login')