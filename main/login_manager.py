import flask_login
from flask import redirect, url_for
from .settings import main_app
from registration.models import User


main_app.secret_key = "KEY"
login_manager = flask_login.LoginManager(app=main_app)
login_manager.login_view = "login"


@login_manager.user_loader
def load_user(id):
    return User.query.get(id)


@main_app.route('/logout', methods=['POST'])
@flask_login.login_required
def logout():
    flask_login.logout_user()
    return redirect("/login")
