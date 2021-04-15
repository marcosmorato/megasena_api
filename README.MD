# Mega-Sena API

    This app is designed to make the user's CRUD, create Mega-Sena games randomly for the logged user, lists all his games, compare with the last draw of the Mega-Sena and return how many numbers the user hit.

## install

    **pip example:**
    pip install --require-hashes -r requirements.txt

    **poetry example:**
    poetry install

## run the app

    flask run

## run the tests

    pytest

# REST API

Example of the REST API for the application below.

## Create New User

# Request

`POST /register`

    http://localhost:5001/register
    {"email": "sasuke@hotmail.com",
    "password": "123456",
    "first_name": "Sasuke",
    "last_name": "Uchiha"}

# Response

    POST /register HTTP/1.1"
    Date: [15/Apr/2021 15:14:42]
    Status: 201
    Connection: close
    Content-Type: application/json

    {"user": {
    "email": "sasuke@hotmail.com",
    "first_name": "Sasuke",
    "last_name": "Uchiha
    "access_token": <jwt_token>,
    "fresh_token": <jwt_token>}}

## Login the user

# Request

`Post /login`

    http://localhost:5001/login
    {"email": "sasuke@hotmail.com",
    "password": "123456",}

# Response

    POST /login HTTP/1.1
    Date: [15/Apr/2021 16:22:23]
    Status 200
    Connection: close
    Content-Type: application/json

    {"access_token": <jwt_token>,
    "fresh_token": <jwt_token>}

## Edit the user

# Request

`Patch /users`

    http://localhost:5001/users
    {"email": "naruto@hotmail.com",
    "first_name": "Naruto",
    "last_name": "Uzumaki,
    "password": "654321"}
    header: Authorization: Bearer <jwt_token>

# Response

    PATCH /users HTTP/1.1"
    Date: [15/Apr/2021 17:04:06]
    Status 200
    Connection: close
    Content-Type: application/json

    {"user": {
        "email": "naruto@hotmail.com",
        "first_name": "Naruto",
        "last_name": "Uzumaki}}

## Delete the User

# Request

`Delete /users`

    http://localhost:5001/users
    header: Authorization: Bearer <jwt_token>

# Response

    DELETE /users HTTP/1.1"
    Date: [15/Apr/2021 17:11:00]
    Status 204
    Connection: close

    {}

## Refresh token

# Request

`GET /refresh`

    http://localhost:5001/refresh
    header: Authorization: Bearer <jwt_token_refresh>

# Response

    GET /refresh HTTP/1.1"
    Date: [15/Apr/2021 17:26:30]
    Status 200
    Connection: close

    {"refresh_token": <jwt_token_refresh>}

## Creating a new game

# Request

`Post /megasena/newgame`

    http://localhost:5001/megasena/newgame
    {"balls": 10}
    header: Authorization: Bearer <jwt_token>

# Response

    POST /megasena/newgame HTTP/1.1
    Date: [15/Apr/2021 17:40:16]
    Status 200
    Connection: close

    {"game": {
    "date": "Thu, 15 Apr 2021 20:40:16 GMT",
    "id_game": 23,
    "numbers": "06,12,43,20,14,15"}}

## Take the result of the megasena

# Request

`Get /megasena/result`

    http://localhost:5001/megasena/result
    header: Authorization: Bearer <jwt_token>

# Response

    POST /megasena/newgame HTTP/1.1"
    Date: [15/Apr/2021 17:40:16]
    Status 200
    Connection: close

    {"result": ["03","20","22","32","35","50"]}

## Shows all games made by the user

# Request

`Get /megasena/my-games`

    http://localhost:5001/megasena/my-games
    header: Authorization: Bearer <jwt_token>

# Response

    GET /megasena/my-games HTTP/1.1
    Date: [15/Apr/2021 17:52:26]
    Status: 200

    {"games": [["50","30","45","49","41","31"],
    ["45","49","33","15","25","34"],
    ["21","08","47","16","26","59","41","31"]]}

## Check how many numbers the user got right

# Request

`Get /megasena/hits`

    http://localhost:5001/megasena/hits
    header: Authorization: Bearer <jwt_token>

# Response

    GET /megasena/hits HTTP/1.1
    Date: [15/Apr/2021 17:58:10]
    Status: 200

    {"hits": ["20"],
    "number_of_hits": 1}
