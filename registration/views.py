import flask
from .models import User
from main.settings import DATABASE

def render_registration():
    if flask.request.method == "POST":
        user = User(name = flask.request.form["name"], password = flask.request.form["password"])
        DATABASE.session.add(user)
        DATABASE.session.commit()
    return flask.render_template(template_name_or_list= "registration.html")