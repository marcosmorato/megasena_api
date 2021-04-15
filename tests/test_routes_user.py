from pytest import fail
from werkzeug.exceptions import NotFound


def test_route_register_exist(app_adapter):
    try:
        app_adapter.match("/register", method="POST")
    except NotFound:
        fail('The application does not contain the route "/register"')


def test_route_login_exist(app_adapter):
    try:
        app_adapter.match("/login", method="POST")
    except NotFound:
        fail('The application does not contain the route "/login"')


def test_route_edit_exist(app_adapter):
    try:
        app_adapter.match("/users", method="PATCH")
    except NotFound:
        fail('The application does not contain the route "/users"')


def test_route_delete_exist(app_adapter):
    try:
        app_adapter.match("/users", method="DELETE")
    except NotFound:
        fail('The application does not contain the route "/users"')
