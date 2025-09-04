import pytest
import allure

from data.generators import generate_create_user_data
from data.message_error import MessageError
from methods.user_methods import UserMethods

@allure.feature('API: Пользователь')
@allure.story('Регистрация пользователя')
class TestUserMethods:
    @allure.title('Успешная регистрация уникального пользователя')
    def test_create_uniq_user_success(self, delete_user):
        user_body = generate_create_user_data()
        with allure.step('Отправляем запрос на рнгистрацию уникального пользователя'):
            response = UserMethods.create_user(user_body)
        with allure.step('Проверяем, что возвращается код 200'):
            assert response.status_code == 200
        with allure.step('Проверяем, что в ответе success: true'):
            assert response.json()['success'] is True
        with allure.step('Проверяем, что email и имя совпадают с отправленными'):
            assert response.json()["user"]["email"] == user_body["email"]
            assert response.json()["user"]["name"] == user_body["name"]
        with allure.step('Проверяем, что в ответе есть accessToken'):
            assert "accessToken" in response.json()
        token = response.json()['accessToken']
        delete_user.append(token)

    @allure.title('Нельзя зарегистрировать пользователя с существующим логином')
    def test_cannot_create_duplicate_user(self, delete_user):
        user_body = generate_create_user_data()
        with allure.step('Регистрируем пользователя в первый раз'):
            first_response = UserMethods.create_user(user_body)
        token = first_response.json()['accessToken']
        delete_user.append(token)
        with allure.step('Повторно отправляем запрос на регистрацию с теми же данными'):
            second_response = UserMethods.create_user(user_body)
        with allure.step('Проверяем, что первый запрос успешный: получаем код 200 и в ответе success: true'):
            assert first_response.status_code == 200
            assert first_response.json()['success'] is True
        with allure.step('Проверяем, что при создании дубликата пользователя код ответ 403 и success: false'):
            assert second_response.status_code == 403
            assert second_response.json()['success'] is False
        with allure.step(f'Проверяем сообщение об ошибке:{MessageError.USER_ALREADY_EXISTS}'):
            assert second_response.json()['message'] == MessageError.USER_ALREADY_EXISTS

    @allure.title('Нельзя зарегистрировать пользователя без заполнения обязательного поля')
    @pytest.mark.parametrize('field', ['email', 'password', 'name'])
    def test_cannot_create_user_with_empty_field(self, field):
        user_body = generate_create_user_data()
        with allure.step(f'Удаляем обязательное поле: {field}'):
            del user_body[field]
        with allure.step('Отправляем запрос на регистрацию пользователя'):
            response = UserMethods.create_user(user_body)
        with allure.step('Проверяем, что при регистрации пользователя без обязательного поля код ответ 403 и success: false'):
            assert response.status_code == 403
            assert response.json()['success'] is False
        with allure.step(f'Проверяем сообщение об ошибке:{MessageError.EMPTY_FIELDS}'):
            assert response.json()['message'] == MessageError.EMPTY_FIELDS




