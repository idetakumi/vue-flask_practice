from flask import Flask, Blueprint, redirect, url_for
from flask_cors import CORS
import requests
from flask_sqlalchemy import SQLAlchemy 
from flask_login import LoginManager, current_user, login_user, logout_user, login_required
import os
from flask import render_template
from backend.config import BaseConfig
from flask_bootstrap import Bootstrap


app = Flask('FLASK-VUE',
        static_folder = BaseConfig.STATIC_DIR,
        template_folder = BaseConfig.DIST_DIR)
app.config.from_object('backend.config.BaseConfig')

db = SQLAlchemy(app) 
db.init_app(app)
db.app = app
bootstrap = Bootstrap(app)

login_manager = LoginManager()
login_manager.init_app(app)

from backend.models.user import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

# 未認証の際のリダイレクト先を設定
@login_manager.unauthorized_handler
def unauthorized_callback():
    return redirect(url_for('app.login'))

from backend.view import view
app.register_blueprint(view, url_prefix="/-")

from backend.api import api
js = Blueprint("javascript", __name__, static_url_path='/javascript', static_folder='template/static/js')
css = Blueprint("css", __name__, static_url_path='/css', static_folder='template/static/css')
image = Blueprint("image", __name__, static_url_path='/image', static_folder='template/static/img')
app.register_blueprint(js)
app.register_blueprint(css)
app.register_blueprint(image)
app.register_blueprint(api, url_prefix="/api")
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
@login_required
def catch_all(path):
#     if app.debug:
#         return requests.get('http://localhost:8080/{}'.format(path)).text
    return render_template("index.html")