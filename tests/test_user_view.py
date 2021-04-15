from flask.app import Flask
from flask.testing import FlaskClient
from flask_jwt_extended.utils import get_unverified_jwt_headers
from pytest import fixture, fail
from faker import Faker
from http import HTTPStatus

ROUTE_REGISTER = "/register"
ROUTE_LOGIN = "/login"
ROUTE_USERS = "/users"


@fixture(scope="module")
def new_user_data():

    fake = Faker()

    yield {
        "email": fake.email(),
        "password": fake.password(),
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
    }


def test_should_create_user(app_client: FlaskClient, new_user_data):

    res = app_client.post(ROUTE_REGISTER, json=new_user_data)

    assert res.status_code == HTTPStatus.CREATED

    response_new_user = res.get_json()
    del response_new_user["user"]["access_token"]
    del response_new_user["user"]["fresh_token"]

    expected = {
        "user": {
            "first_name": new_user_data["first_name"],
            "last_name": new_user_data["last_name"],
            "email": new_user_data["email"],
        }
    }

    assert response_new_user == expected


def test_should_not_create_user(app_client: FlaskClient, new_user_data):
    res_duplicate_value = app_client.post(ROUTE_REGISTER, json=new_user_data)

    assert res_duplicate_value.status_code == HTTPStatus.BAD_REQUEST

    bad_incomplete_body = {
        "email": "test123@hotmail.com",
        "first_name": "test",
        "last_name": "test",
    }

    res_incomplete_data = app_client.post(ROUTE_REGISTER, json=bad_incomplete_body)

    assert res_incomplete_data.status_code == HTTPStatus.BAD_REQUEST


def test_should_login(app_client: FlaskClient, new_user_data):
    login_body = {
        "email": new_user_data["email"],
        "password": new_user_data["password"],
    }

    res_successful_login = app_client.post(ROUTE_LOGIN, json=login_body)

    assert res_successful_login.status_code == HTTPStatus.OK


def test_should_not_login(app_client: FlaskClient):
    incomplete_body = {"email": "teste123@hotmail.com"}

    res_incomplete_body = app_client.post(ROUTE_LOGIN, json=incomplete_body)

    assert res_incomplete_body.status_code == HTTPStatus.BAD_REQUEST

    invalid_body = {"email": "teste123@hotmail.com", "password": "1234567895"}

    res_invalid_body = app_client.post(ROUTE_LOGIN, json=invalid_body)

    assert res_invalid_body.status_code == HTTPStatus.BAD_REQUEST
