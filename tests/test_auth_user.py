import pytest
import allure


from data.message_error import MessageError
from methods.user_methods import UserMethods

@allure.feature('API: Авторизация пользователя')
class TestAuthUser:
    @allure.title('Успешная авторизация пользователя')
    @allure.description('Проверяем, что зарегистрированный пользователь может успешно авторизоваться')
    def test_success_auth_user(self, create_and_delete_user):
        email, password = create_and_delete_user
        with allure.step('Отправляем запрос на авторизацию с валидными данными'):
            auth_response = UserMethods.login_user(email, password)
        with allure.step('Проверяем, что сервер возвращает статус 200 и success: true'):
            assert auth_response.status_code == 200
            assert auth_response.json()['success'] is True
        with allure.step('Проверяем, что в ответе есть accessToken'):
            assert "accessToken" in auth_response.json()
        with allure.step('Проверяем, что в ответе есть refreshToken'):
            assert "refreshToken" in auth_response.json()
        with allure.step('Проверяем, что email в ответе совпадает с отправленным'):
            assert auth_response.json()["user"]["email"] == email

    @allure.title('Ошибка при неверном email')
    @allure.description('Проверяем, что нельзя авторизоваться с несуществующим email')
    def test_auth_user_invalid_email_failed(self, create_and_delete_user):
        email, password = create_and_delete_user
        with allure.step('Отправка запроса на авторизацию с несуществующим email'):
            auth_response = UserMethods.login_user('nonemail@mail.ru', password)
        with allure.step('Проверяем, что при создании пользователя без обязательного поля код ответ 401 и success: false'):
            assert auth_response.status_code == 401
            assert auth_response.json()['success'] is False
        with allure.step(f'Проверяем что сообщение об ошибке: {MessageError.INCORRECT_FIELDS}'):
            assert auth_response.json()['message'] == MessageError.INCORRECT_FIELDS

    @allure.title('Ошибка при неверном пароле')
    @allure.description('Проверяем, что нельзя авторизоваться с несуществующим паролем')
    def test_auth_user_invalid_password_failed(self, create_and_delete_user):
        email, password = create_and_delete_user
        with allure.step('Отправка запроса на авторизацию с несуществующим паролем'):
            auth_response = UserMethods.login_user(email, 'nonepassword')
        with allure.step('Проверяем, что при создании пользователя без обязательного поля код ответ 401 и success: false'):
            assert auth_response.status_code == 401
            assert auth_response.json()['success'] is False
        with allure.step(f'Проверяем что сообщение об ошибке: {MessageError.INCORRECT_FIELDS}'):
            assert auth_response.json()['message'] == MessageError.INCORRECT_FIELDS

