import flask, flask_login
from registration.models import Tour


def render_tour():
    return flask.render_template(template_name_or_list="tour.html", all_tours = Tour.query.all(), flask_login = flask_login)