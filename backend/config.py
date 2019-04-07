import os
from backend import app
class BaseConfig(object):
    DEBUG = True
    ## 以下を追記
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or "postgresql://postgres:postgres@localhost:5432/flask_db"
    # cookieを暗号化する秘密鍵
    SECRET_KEY = os.urandom(24)