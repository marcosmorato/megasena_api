from flask import Flask
from os import getenv
from config import config_select

from app import views

from app.configurations import database, migrate, authentication


def create_app():

    app = Flask(__name__)
    config_type = getenv("FLASK_ENV")

    app.config.from_object(config_select[config_type])

    database.init_app(app)
    migrate.init_app(app)
    authentication.init_app(app)
    views.init_app(app)

    return app
