from flask import Blueprint, abort, session, request, current_app, redirect, render_template
from mygitlab.forms import GitlabForm
import gitlab


auth = Blueprint('auth', __name__)


def send_user_to_dataservice(email, access_token):
    pass


@auth.route('/gitlab_login', methods=['GET', 'POST'])
def gitlab_login():
    form = GitlabForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            access_token = form.data['gitlab_token']
            gl = gitlab.Gitlab('https://umcs.schneiderp.ovh', access_token)
            gl.auth()
            guser = gl.user
            email = guser.email
            send_user_to_dataservice(email, access_token)
            session['user'] = email
            session['token'] = access_token
            return redirect('/')

    return render_template('gitlab_login.html', form=form)


@auth.route('/logout')
def logout():
    if 'user' in session:
        del session['user']
        del session['token']
    return redirect('/')


