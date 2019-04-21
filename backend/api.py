from flask import Blueprint, jsonify, request
from random import *
from flask_cors import CORS
from flask import make_response
from flask_login import current_user

from backend import db
from backend.models.task import Task
from backend.models.user import User

api = Blueprint('api', __name__)

@api.route('/get', methods=['GET'])
def get_taks():
    taks = Task.query.filter(Task.user_id==current_user.id).order_by(Task.id.desc()).all()
    taks_dict = [task.to_dict() for task in taks]
    return jsonify(taks_dict)

@api.route('/add', methods=['POST'])
def add_task():
    task = Task(
        title=request.form['title'],
        text=request.form['text'],
        user_id=current_user.id,
        priority=request.form['priority']
        )
    db.session.add(task)
    db.session.commit()
    task = Task.query.filter(User.id==current_user.id).order_by(Task.id.desc()).first()
    id = str(task.id)
    r = make_response(id)
    return r

@api.route('/delete', methods=['POST'])
def delete_task():
    id = request.form['id']
    task = Task.query.get(id)
    db.session.delete(task)
    db.session.commit()
    r = make_response(id)
    return r

@api.route('/update', methods=['POST'])
def update_task():
    id = request.form['id']
    task = db.session.query(Task).filter(Task.id==id).first()
    task.title = request.form['title']
    task.text = request.form['text']
    task.priority = request.form['priority']
    db.session.commit()
    r = make_response(id)
    return r