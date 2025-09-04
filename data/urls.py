class Urls:
    """ Базовый URL"""
    BASE_URL = 'https://stellarburgers.nomoreparties.site'


    """ Эндпоинты для Создания/Авторизации/Удаления пользователя"""
    CREATE_USER = f'{BASE_URL}/api/auth/register' # Создание пользователя ручкой POST
    AUTH_USER = f'{BASE_URL}/api/auth/login' # Авторизация пользователя ручкой POST
    DELETE_USER = f'{BASE_URL}/api/auth/user' # Удаление пользователя ручкой DELETE

    """ Эндпоинт для создания заказа"""
    CREATE_ORDER = f'{BASE_URL}/api/orders' # Создание заказа ручкой POST





