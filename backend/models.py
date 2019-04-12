from backend import db, app

class Task(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    text = db.Column(db.Text)

    def to_dict(self):
        return dict(
            id=self.id,
            title=self.title,
            text=self.text
        )

    def __repr__(self):
        return '<Task id={id} title={title!r}>'.format(
            id=self.id, title=self.title)

def init():
    with app.app_context():
        db.create_all()