from collections import UserString

import pytest
from data.generators import generate_create_user_data
from methods.user_methods import UserMethods

@pytest.fixture(scope='function')
def create_and_delete_user():
    user_body = generate_create_user_data()
    email = user_body['email']
    password = user_body['password']
    response_create = UserMethods.create_user(user_body)
    token = response_create.json()['accessToken']
    yield email, password
    UserMethods.delete_user(token)

@pytest.fixture(scope='function')
def delete_user():
    user_tokens = []
    yield user_tokens
    for token in user_tokens:
        UserMethods.delete_user(token)


