import gitlab
import requests

# from celery import Celery
# BACKEND = BROKER = 'redis://localhost:6379'
# celery = Celery(__name__, backend=BACKEND, broker=BROKER)

DATASERVICE = 'http://127.0.0.1:5002'


def fetch_all_projects():
    users = requests.get(DATASERVICE + '/users').json()['users']
    projects_fetched = {}

    for user in users:
        gitlab_token = user.get('gitlab_token')
        email = user['email']

        if gitlab_token is None:
            continue

        print('Fetching Gitlab for %s' % email)
        #projects_fetched[user['id']] = fetch_projects(user)
        projects_fetched['5'] = fetch_projects(user)

    return projects_fetched


def push_to_dataservice(projects):
    requests.post(DATASERVICE + '/add_projects', json=projects)


def project2db(user, user_project):
    """Used by fetch_projects to convert a Gitlab entry.
    """
    project = {}
    project['gitlab_id'] = user_project.id
    project['name'] = user_project.name
    project['description'] = user_project.description
    project['visibility'] = user_project.visibility
    project['ssh_url_to_repo'] = user_project.ssh_url_to_repo
    project['http_url_to_repo'] = user_project.http_url_to_repo
    project['web_url'] = user_project.web_url
    project['name_with_namespace'] = user_project.name_with_namespace
    project['path'] = user_project.path
    project['path_with_namespace'] = user_project.path_with_namespace
    project['created_at'] = user_project.created_at
    project['last_activity_at'] = user_project.last_activity_at

    return project


def fetch_projects(user):
    gl = gitlab.Gitlab('https://umcs.schneiderp.ovh', private_token=user['gitlab_token'])
    projects = []

    all_projects = gl.projects.list(all=True)
    for project in all_projects:
        projects.append(project2db(user, project))
    return projects


if __name__ == '__main__':
    push_to_dataservice(fetch_all_projects())
