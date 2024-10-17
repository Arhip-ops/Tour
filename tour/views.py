import flask 
from registration.models import Tour


def render_tour():
    return flask.render_template(template_name_or_list="tour.html", all_tours = Tour.query.all())