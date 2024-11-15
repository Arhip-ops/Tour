import flask
from registration.models import User
import flask_login

def render_login():
    if flask.request.method == "POST":
        for user in User.query.filter_by(name = flask.request.form["name"]):
            if user.password == flask.request.form["password"]:
                flask_login.login_user(user)

    return flask.render_template(template_name_or_list="login.html", flask_login = flask_login)