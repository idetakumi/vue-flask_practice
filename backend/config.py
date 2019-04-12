import os

class BaseConfig(object):
    DEBUG = True
    ## 以下を追記
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or "postgresql://postgres:postgres@localhost:5432/flask_db"
    # cookieを暗号化する秘密鍵
    SECRET_KEY = os.urandom(24)
    # If not set fall back to production for safety
    FLASK_ENV =  os.getenv('FLASK_ENV', 'production')
    # Set FLASK_SECRET on your production Environment
    SECRET_KEY = os.getenv('FLASK_SECRET', 'Secret')
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    APP_DIR = os.path.dirname(__file__)
    ROOT_DIR = os.path.dirname(APP_DIR)
    DIST_DIR = os.path.join(ROOT_DIR, 'templates')
    STATIC_DIR = os.path.join(DIST_DIR, 'static')

    if not os.path.exists(DIST_DIR):
        raise Exception(
            'DIST_DIR not found: {}'.format(DIST_DIR))
