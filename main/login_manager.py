import flask_login
from .settings import main_app
from registration.models import User

main_app.secret_key = "KEY"

login_manager = flask_login.LoginManager(app=main_app)

login_manager.login_view = "login"

@login_manager.user_loader
def load_user(id):
    return User.query.get(id)