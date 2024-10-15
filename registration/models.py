import flask
import flask_login
from main.settings import DATABASE

class User(DATABASE.Model, flask_login.UserMixin):
    id = DATABASE.Column(DATABASE.Integer, primary_key = True)
    name = DATABASE.Column(DATABASE.String(50), nullable = False)
    password = DATABASE.Column(DATABASE.String(256), nullable = False)
    def __repr__(self):
        return f"Ім'я {self.name} {self.password}"