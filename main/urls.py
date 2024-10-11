from .settings import main_app
import home

home.home_app.add_url_rule(
    rule = "/",
    view_func = home.render_home,
    methods = ['GET', 'POST']
)

main_app.register_blueprint(blueprint = home.home_app)