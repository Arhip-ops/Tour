import flask
import flask_sqlalchemy
import flask_migrate
import os

main_app = flask.Flask(
    import_name="main",
    template_folder="templates",
    instance_path= os.path.abspath(__file__ + "/..")
)

main_app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"

# Ініціалізація SQLAlchemy
DATABASE = flask_sqlalchemy.SQLAlchemy(app=main_app)

# Ініціалізація Flask-Migrate для керування міграціями
MIGRATE = flask_migrate.Migrate(app=main_app, db=DATABASE)