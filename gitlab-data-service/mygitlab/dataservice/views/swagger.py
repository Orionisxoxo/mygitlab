import os
from datetime import datetime

from flakon import SwaggerBlueprint
from flask import request, jsonify
from mygitlab.dataservice.database import db, User, Project


HERE = os.path.dirname(__file__)
YML = os.path.join(HERE, '..', 'static', 'api.yaml')
api = SwaggerBlueprint('API', __name__, swagger_spec=YML)


@api.operation('addProjects')
def add_projects():
    # each project has the user id
    # it's controlled & pushed in the DB
    # XXX controls
    # dupes
    added = 0
    for user, projects in request.json.items():
        user_id = int(user)
        for project in projects:
            db_project = Project()
            db_project.gitlab_id = project['gitlab_id']
            db_project.description = project['description']
            db_project.visibility = project['visibility']
            db_project.name = project['name']
            db_project.ssh_url_to_repo = project['ssh_url_to_repo']
            db_project.http_url_to_repo = project['http_url_to_repo']
            db_project.web_url = project['web_url']
            db_project.name_with_namespace = project['name_with_namespace']
            db_project.path = project['path']
            db_project.path_with_namespace = project['path_with_namespace']
            #db_project.created_at = datetime.fromtimestamp(project['created_at'])
            #db_project.last_activity_at = datetime.fromtimestamp(project['last_activity_at'])
            db_project.created_at = project['created_at']
            db_project.last_activity_at = project['last_activity_at']
            db_project.user_id = user_id
            db.session.add(db_project)

            added += 1

    if added > 0:
        db.session.commit()

    return {'added': 1}


@api.operation('getProjects')
def get_projects(user_id):
    projects = db.session.query(Project).filter(Project.user_id == user_id)
    return jsonify([project.to_json() for project in projects])


@api.operation('getUsers')
def get_users():
    users = db.session.query(User)
    page = 0
    page_size = None
    if page_size:
        users = users.limit(page_size)
    if page != 0:
        users = users.offset(page * page_size)
    return {'users': [user.to_json(secure=True) for user in users]}
