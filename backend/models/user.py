from flask_login import UserMixin
from flask_wtf import FlaskForm
from wtforms import TextField, PasswordField, validators
from sqlalchemy.orm import synonym
from werkzeug import check_password_hash, generate_password_hash

from backend import db

class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    userName = db.Column(db.String(255), unique=True, nullable=False)
    _password = db.Column('password', db.String(255), nullable=False)
    active = db.Column(db.Boolean(), default=True)

    def _get_password(self):
        return self._password

    def _set_password(self, password):
        if password:
          password = password.strip()
        self._password = generate_password_hash(password)
        password_descriptor = property(_get_password, _set_password)
        password = synonym('_password', descriptor=password_descriptor)
    
    # フォームで送信されたパスワードの検証
    def check_password(self, password):
        password = password.strip()
        if not password:
            return False
        return check_password_hash(self._password, password)

    # 認証処理
    @classmethod
    def auth(cls, query, userName, password):
        user = query(cls).filter(cls.userName==userName).first()
        if user is None:
            return None, False
        return user, user.check_password(password)