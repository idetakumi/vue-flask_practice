from flask import Flask, Blueprint
from flask_cors import CORS
import requests
from flask_sqlalchemy import SQLAlchemy 
import os
from flask import render_template
from backend.config import BaseConfig


app = Flask('FLASK-VUE',
        static_folder = BaseConfig.STATIC_DIR,
        template_folder = BaseConfig.DIST_DIR)
app.config.from_object('backend.config.BaseConfig')

db = SQLAlchemy(app) 
db.init_app(app)
db.app = app

from backend.api import api
js = Blueprint("javascript", __name__, static_url_path='/javascript', static_folder='template/static/js')
css = Blueprint("css", __name__, static_url_path='/css', static_folder='template/static/css')
image = Blueprint("image", __name__, static_url_path='/image', static_folder='template/static/img')
app.register_blueprint(js)
app.register_blueprint(css)
app.register_blueprint(image)
app.register_blueprint(api, url_prefix="/api")
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})



# @app.route('/')
# def index_client():
#     dist_dir = current_app.config['DIST_DIR']
#     entry = os.path.join(dist_dir, 'index.html')
#     return send_file(entry)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    if app.debug:
        return requests.get('http://localhost:8080/{}'.format(path)).text
    return render_template("index.html")