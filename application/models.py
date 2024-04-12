from flask_sqlalchemy import SQLAlchemy
from flask_security import UserMixin, RoleMixin
db = SQLAlchemy()

class RolesUsers(db.Model):
    __tablename__ = 'roles_users'
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column('user_id', db.Integer(), db.ForeignKey('user.id'))
    role_id = db.Column('role_id', db.Integer(), db.ForeignKey('role.id'))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=False)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    fs_uniquifier = db.Column(db.String(255), unique=True, nullable=False)
    roles = db.relationship('Role', secondary='roles_users', backref=db.backref('users', lazy='dynamic'))
    # playlists = db.relationship('Playlists', backref='creator')

class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

class Album(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    album_name = db.Column(db.String, nullable=False)
    artist = db.Column(db.String)

class Songs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    song_name = db.Column(db.String, nullable=False)
    lyrics = db.Column(db.String)
    genre = db.Column(db.String, nullable=False)
    duration = db.Column(db.Date)
    date_created = db.Column(db.Date)
    resource_link = db.Column(db.String, nullable=False)

class Playlists(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    playlist_name = db.Column(db.String, nullable=False)
    playlist_description = db.Column(db.String, nullable=True)
    # creator_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)