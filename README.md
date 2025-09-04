# Дипломный проект. 2 задание
# Вятских Илья
# Когорта 27FS

# 🛵 API-тесты для Stellar Burgers

Проект по автоматизированному тестированию API сервиса **Stellar Burgers** — платформы для заказа бургеров.

---

## 🧪 Тестируемые сценарии

### 1. Регистрация пользователя (`POST /api/auth/register`)

- ✅ `test_create_uniq_user_success` — успешная регистрация нового пользователя  
- ✅ `test_cannot_create_duplicate_user` — нельзя зарегистрировать существующего пользователя  
- ✅ `test_cannot_create_user_with_empty_field` — нельзя зарегистрировать без одного из обязательных полей

### 2. Авторизация пользователя (`POST /api/auth/login`)

- ✅ `test_success_auth_user` — зарегистрированный пользователь может успешно авторизоваться  
- ✅ `test_auth_user_invalid_email_failed` — нельзя авторизоваться с неверным email  
- ✅ `test_auth_user_invalid_password_failed` — нельзя авторизоваться с неверным паролем

### 3. Создание заказа (`POST /api/orders`)

- ✅ `test_create_order_auth_user_success` — авторизованный пользователь может создать заказ  
- ✅ `test_create_order_unauth_user_failed` — неавторизованный пользователь не может создать заказ  
- ✅ `test_create_order_with_invalid_ingredient_failed` — нельзя создать заказ с неверным хешем ингредиентов  
- ✅ `test_create_order_without_ingredient_failed` — нельзя создать заказ без ингредиентов

---

## 🗂 Структура проекта
````
Diplom_2/
├── data/ # 📄 URL, данные
│ ├── init.py
│ ├── urls.py # 🌐 Базовые URL эндпоинтов
│ ├── generators.py # 🎲 Генераторы данных (email, пароль, имя)
│ ├── ingredients_data.py # 🧫 Валидные и невалидные ID ингредиентов
│ └── message_error.py # ❌ Сообщения об ошибках из API
│
├── methods/ # 🧩 Методы для взаимодействия с API
│ ├── init.py
│ ├── user_methods.py # 🔐 Регистрация, авторизация, удаление
│ └── order_methods.py # 📦 Создание заказа
│
├── tests/ # ✅ Тесты
│ ├── init.py
│ ├── conftest.py # 🔁 Фикстуры: create_and_delete_user, delete_user
│ ├── test_create_user.py # 👤 Тесты на регистрацию
│ ├── test_auth_user.py # 🔐 Тесты на авторизацию
│ └── test_create_order.py # 🍔 Тесты на создание заказа
│
├── .gitignore # 🚫 Игнорируемые файлы (.venv, pycache, etc.)
├── requirements.txt # ⚙️ Зависимости: pytest, requests, allure, faker
├── README.md # 📘 Этот файл
└── pytest.ini # 🛠 Конфигурация pytest (опционально)
````