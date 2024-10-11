import flask
from flask_mail import Message
from main.mail_config import ADMINISTRATION_ADRESS, mail 

def render_home():
    if flask.request.method ==  "POST":
        name = flask.request.form["name"]
        email = flask.request.form["email"]
        review = flask.request.form["review"]
        message = Message("message_order",
                           sender = ADMINISTRATION_ADRESS,
                           recipients = ["touragency10.00@gmail.com"],
                           body = f"Кліент {name} залишив/ла відгук:\n {review}.\n Пошта для зворотнього зв'язку з клієнтом {email}.")

        mail.send(message)
    return flask.render_template(template_name_or_list = "home.html")
