from os import getenv
from environs import Env
from secrets import token_hex

env = Env()
env.read_env()


class Config:
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = token_hex(32)
    JSON_SORT_KEYS = getenv("JSON_SORT_KEYS")
    FLASK_RUN_PORT = getenv("FLASK_RUN_PORT")


class Development(Config):
    ENV = "development"
    SQLALCHEMY_DATABASE_URI = getenv("SQLALCHEMY_DATABASE_URI")


class Production(Config):
    ...


class Test(Config):
    ENV = "testing"
    SQLALCHEMY_DATABASE_URI = getenv("SQLALCHEMY_DATABASE_URI_TEST")
    TESTING = True


config_select = {
    "development": Development,
    "production": Production,
    "test": Test,
}
