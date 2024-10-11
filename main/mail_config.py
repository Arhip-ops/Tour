import flask_mail
from .settings import main_app

ADMINISTRATION_ADRESS = "artemvaschenko83@gmail.com"
ADMINISTRATION_PASSWORD = "sncj nczy toqt atlm"
main_app.config["MAIL_SERVER"] = "smtp.gmail.com"
main_app.config["MAIL_PORT"] = 587
main_app.config["MAIL_USE_TLS"] = True
main_app.config["MAIL_USERNAME"] = ADMINISTRATION_ADRESS
main_app.config["MAIL_PASSWORD"] = ADMINISTRATION_PASSWORD
mail = flask_mail.Mail(main_app)