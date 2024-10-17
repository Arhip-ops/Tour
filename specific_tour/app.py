import flask

specific_tour_app = flask.Blueprint(
    name="specific_tour_app",
    import_name="specific_tour",
    template_folder="templates"
)