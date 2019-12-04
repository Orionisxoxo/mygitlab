from flask import Blueprint, session, render_template
from flask import current_app as app


home = Blueprint('home', __name__)


@home.route('/')
def index():
    user = session.get('user')
    return render_template('index.html', user=user)


