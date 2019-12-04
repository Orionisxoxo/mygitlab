from flask_wtf import FlaskForm
import wtforms as f
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    email = f.StringField('email', validators=[DataRequired()])
    password = f.PasswordField('password', validators=[DataRequired()])
    display = ['email', 'password']


class GitlabForm(FlaskForm):
    gitlab_token = f.StringField('gitlab_token')

    display = ['gitlab_token']
