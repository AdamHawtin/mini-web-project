import os

from flask import Flask
from flask_cors import CORS

import config


def create_app():
    app = Flask(__name__)
    CORS(app)
    app_config = getattr(config, os.getenv('APP_SETTINGS', 'Config'))
    app.config.from_object(app_config)
    add_blueprints(app)

    return app


def add_blueprints(app):

    from app.api.health import health_blueprint
    from app.views.index import index_blueprint

    app.register_blueprint(health_blueprint)
    app.register_blueprint(index_blueprint)
