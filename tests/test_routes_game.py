from pytest import fail
from werkzeug.exceptions import NotFound


def test_route_register_exist(app_adapter):
    try:
        app_adapter.match("/megasena/newgame", method="POST")
    except NotFound:
        fail('The application does not contain the route "/megasena/newgame"')


def test_route_result_exist(app_adapter):
    try:
        app_adapter.match("/megasena/result", method="GET")
    except NotFound:
        fail('The application does not contain the route "/megasena/result"')


def test_route_hits_exist(app_adapter):
    try:
        app_adapter.match("/megasena/hits", method="GET")
    except NotFound:
        fail('The application does not contain the route "/megasena/hits"')


def test_route_my_games_exist(app_adapter):
    try:
        app_adapter.match("/megasena/my-games", method="GET")
    except NotFound:
        fail('The application does not contain the route "/megasena/my-games"')
