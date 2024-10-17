import flask
import flask_login
from main.settings import DATABASE

class User(DATABASE.Model, flask_login.UserMixin):
    id = DATABASE.Column(DATABASE.Integer, primary_key = True)
    name = DATABASE.Column(DATABASE.String(50), nullable = False)
    password = DATABASE.Column(DATABASE.String(256), nullable = False)
    def __repr__(self):
        return f"Ім'я {self.name} {self.password}"

class Tour(DATABASE.Model):
    id = DATABASE.Column(DATABASE.Integer, primary_key = True)
    title = DATABASE.Column(DATABASE.String(256), nullable = False)
    date = DATABASE.Column(DATABASE.String(10), nullable = False)
    country = DATABASE.Column(DATABASE.String(100), nullable = False)    
    price = DATABASE.Column(DATABASE.Integer, nullable = False)
    description = DATABASE.Column(DATABASE.String(500), nullable = False)
