# database modelsssss

from . import db # init.py
from flask_login import UserMixin
from sqlalchemy.sql import func

# notes table
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

# work table
class Work(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    description = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    status = db.Column(db.String(100))
    points = db.Column(db.Integer)

# user table
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(255))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note') # store all notes user has
    team_id = db.Column(db.Integer, db.ForeignKey('team.id'))
    team_leader = db.Column(db.Boolean)
    work = db.relationship('Work') # store all work user has
    points = db.Column(db.Integer)

# teams table
class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    users = db.relationship('User') # store all users here

