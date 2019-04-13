from backend import db


class Task(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    text = db.Column(db.Text)
    user_id = db.Column(db.Integer)

    def to_dict(self):
        return dict(
            id=self.id,
            title=self.title,
            text=self.text,
            user_id=self.user_id
        )

    def __repr__(self):
        return '<Task id={id} title={title!r} user_id={user_id}>'.format(
            id=self.id, title=self.title, user_id=self.user_id)

