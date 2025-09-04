import requests
import allure

from data.urls import Urls

class OrderMethods:
    @staticmethod
    @allure.step('Создание заказа')
    def create_order(order_data):
        response = requests.post(Urls.CREATE_ORDER, json=order_data)
        return response