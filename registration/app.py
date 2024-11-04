import flask

registration_app = flask.Blueprint(
    name = "registration_app",
    import_name = "registration",
    template_folder = "templates",
    static_folder= "static",
    static_url_path= "/registration/"
)