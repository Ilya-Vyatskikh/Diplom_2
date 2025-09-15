import requests
import allure

from data.urls import Urls


class UserMethods:
    @staticmethod
    @allure.step('Регистрация нового пользователя')
    def create_user(create_body):
        return requests.post(Urls.CREATE_USER, json=create_body)

    @staticmethod
    @allure.step('Авторизация пользователя')
    def login_user(email, password):
        response = requests.post(Urls.AUTH_USER, json={'email':email, 'password':password})
        return response

    @staticmethod
    @allure.step('Удаление пользователя')
    def delete_user(token):
        response = requests.delete(Urls.DELETE_USER, headers={'Authorization': token})
        return response