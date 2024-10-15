import flask

login_app = flask.Blueprint(
    name="login_app",
    import_name="login",
    template_folder="templates"
)