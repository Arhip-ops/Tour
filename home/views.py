import flask
from flask_mail import Message
def render_home():
    return flask.render_template(template_name_or_list = "home.html")