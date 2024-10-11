import flask
from flask_mail import Message
from main.email_config import ADMINISTRATION_ADRESS, ADMINISTRATION_PASSWORD, mail
def render_home():
    if flask.request.method == 'POST':
        name = flask.request.form['name']
        email = flask.request.form['email']
        otzuv = flask.request.form['wish']
        print(name, email, otzuv)
        message = Message("message_order", sender = ADMINISTRATION_ADRESS, recipients=["artemvashenko201010@gmail.com"], body= f"{name}, {email}, {otzuv}")
        mail.send(message)
    return flask.render_template(template_name_or_list = "home.html")