from flask import Flask


def create_app():
    app = Flask(__name__)


    from .views import app_

    app.register_blueprint(app_)

    return app
