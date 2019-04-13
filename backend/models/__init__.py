from backend import db, app

def init():
    with app.app_context():
        db.create_all()