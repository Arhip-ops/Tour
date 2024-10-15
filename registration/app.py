import flask

registration_app = flask.Blueprint(
    name = "registration_app",
    import_name = "registration",
    template_folder = "templates"
)