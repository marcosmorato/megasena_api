from flask import Flask
from pytest import fixture
from app import create_app

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from environs import Env

from app.configurations.database import SQLAlchemy


@fixture
def sample_app():
    return create_app()


@fixture
def app_client(sample_app: Flask):
    return sample_app.test_client()


@fixture
def app_adapter(app_client):
    return app_client.application.url_map.bind("")
