# encoding: utf8
import os
from datetime import datetime
from decimal import Decimal
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.Unicode(128), nullable=False)
    firstname = db.Column(db.Unicode(128))
    lastname = db.Column(db.Unicode(128))
    password = db.Column(db.Unicode(128))
    gitlab_token = db.Column(db.String(128))
    is_active = db.Column(db.Boolean, default=True)
    is_admin = db.Column(db.Boolean, default=False)

    is_anonymous = False

    def to_json(self, secure=False):
        res = {}
        for attr in ('id', 'email', 'firstname', 'lastname'):
            value = getattr(self, attr)
            if isinstance(value, Decimal):
                value = float(value)
            res[attr] = value
        if secure:
            res['gitlab_token'] = self.gitlab_token
        return res

    def get_id(self):
        return self.id


class Project(db.Model):
    __tablename__ = 'project'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    description = db.Column(db.Unicode(128))
    visibility = db.Column(db.Unicode(128))
    name = db.Column(db.Unicode(128))
    gitlab_id = db.Column(db.Integer)
    ssh_url_to_repo = db.Column(db.Unicode(128))
    http_url_to_repo = db.Column(db.Unicode(128))
    web_url = db.Column(db.Unicode(128))
    name_with_namespace = db.Column(db.Unicode(128))
    path = db.Column(db.Unicode(128))
    path_with_namespace = db.Column(db.Unicode(128))
    created_at = db.Column(db.String())
    last_activity_at = db.Column(db.String())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user_project = relationship('User', foreign_keys='Project.user_id')

    def to_json(self):
        res = {}
        for attr in ('id', 'description', 'visibility', 'name', 'gitlab_id', 'ssh_url_to_repo', 'http_url_to_repo',
                     'web_url', 'name_with_namespace', 'path', 'path_with_namespace', 'created_at', 'last_activity_at',
                     'user_id'):
            value = getattr(self, attr)
            if isinstance(value, datetime):
                value = value.timestamp()
            res[attr] = value
        return res


class Group(db.Model):
    __tablename__ = 'group'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Unicode(128))
    path = db.Column(db.Unicode(128))
    description = db.Column(db.Unicode(128))
    visibility = db.Column(db.Unicode(128))
    web_url = db.Column(db.Unicode(128))
    full_name = db.Column(db.Unicode(128))
    full_path = db.Column(db.Unicode(128))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user_group = relationship('User', foreign_keys='Group.user_id')

    def to_json(self):
        res = {}
        for attr in ('id', 'name', 'path', 'description', 'visibility',
                     'web_url', 'full_name', 'full_path', 'user_id'):
            value = getattr(self, attr)
            if isinstance(value, datetime):
                value = value.timestamp()
            res[attr] = value
        return res


def init_database():
    exists = db.session.query(User).filter(User.email == 'suser@example.pl')
    if exists.all() != []:
        return

    suser = User()
    suser.email = 'suser@suser.pl'
    suser.firstname = 'Suser'
    suser.lastname = 'Example'
    suser.gitlab_token = os.environ.get('GITLAB_TOKEN')
    db.session.add(suser)
    db.session.commit()
