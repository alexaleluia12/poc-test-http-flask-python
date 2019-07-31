from flask import Flask

from . import app


def create_app(config=None):
    server_instance = Flask(__name__)
    server_instance.register_blueprint(app.blueprint)

    if config:
        server_instance.config.update(config)
    return server_instance
