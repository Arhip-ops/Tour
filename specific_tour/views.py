import flask 


def render_specific_tour():
    return flask.render_template(template_name_or_list="specific_tour.html")