import flask, flask_login
from main.settings import DATABASE
from registration.models import Tour

def render_specific_tour():
    id = flask.request.cookies.get("tour")
    tour = Tour.query.get(id)
    return flask.render_template(template_name_or_list="specific_tour.html", tour = tour, flask_login = flask_login)