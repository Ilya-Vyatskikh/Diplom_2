import pytest
import allure

from data.ingredients_data import IngredientData
from data.message_error import MessageError
from methods.user_methods import UserMethods
from methods.order_methods import OrderMethods

@allure.feature('API: Создание заказа')
@allure.story('Создание заказа на бургера')
class TestCreateOrder:
    @allure.title('Создание заказа автроизованным пользователем')
    def test_create_order_auth_user_success(self, create_and_delete_user):
        email, password = create_and_delete_user
        with allure.step('Авторизуемся зарегистророванным пользователем'):
            UserMethods.login_user(email, password)
        with allure.step('Отправляем запрос на создание заказа с валидными ингредиентами'):
            order_response = OrderMethods.create_order(IngredientData.valid_data)
        with allure.step('Проверяем, что сервер возвращает статус 200 и success: true'):
            assert order_response.status_code == 200
            assert order_response.json()['success'] is True

    @allure.title('Создание заказа неавторизованным пользователем')
    def test_create_order_unauth_user_failed(self):
        with allure.step('Отправляем запрос на создание заказа с валидными данными'):
            order_response = OrderMethods.create_order(IngredientData.valid_data)
        with allure.step('Проверяем, что сервер возвращает статус 401 и success: false'):
            assert order_response.status_code == 401
            assert order_response.json()['success'] is False

    @allure.title('Создание заказа с неверным хэшем ингредиентов')
    def test_create_order_with_invalid_ingredient_failed(self, create_and_delete_user):
        email, password = create_and_delete_user
        with allure.step('Авторизуемся зарегистророванным пользователем'):
            UserMethods.login_user(email, password)
        with allure.step('Отправляем запрос на создание заказа с неверным хэшем ингредиентов'):
            order_response = OrderMethods.create_order(IngredientData.invalid_data)
        with allure.step('Проверяем, что сервер присылает в ответ код 500'):
            assert order_response.status_code == 500

    @allure.title('Создание заказа без ингредиентов')
    def test_create_order_without_ingredient_failed(self, create_and_delete_user):
        email, password = create_and_delete_user
        with allure.step('Авторизуемся зарегистророванным пользователем'):
            UserMethods.login_user(email, password)
        with allure.step('Отправляем запрос на создание заказа без ингредиентов'):
            order_response = OrderMethods.create_order(IngredientData.empty_data)
        with allure.step('Проверяем, что получаем код ответа 400 и success: false'):
            assert order_response.status_code == 400
            assert order_response.json()['success'] is False
        with allure.step(f'Проверяем что сообщение об ошибке: {MessageError.EMPTY_INGREDIENTS}'):
            assert order_response.json()['message'] == MessageError.EMPTY_INGREDIENTS

