from .settings import main_app
import home
import registration
import login

home.home_app.add_url_rule(
    rule = "/",
    view_func = home.render_home,
    methods = ['GET', 'POST']
)
registration.registration_app.add_url_rule(
    rule = "/registration/",
    view_func= registration.render_registration,
    methods = ['POST', 'GET']
)

login.login_app.add_url_rule(
    rule = "/login/",
    view_func = login.render_login,
    methods = ['POST', 'GET']
)
main_app.register_blueprint(blueprint = home.home_app)

main_app.register_blueprint(blueprint = registration.registration_app)

main_app.register_blueprint(blueprint = login.login_app)