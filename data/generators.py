import uuid

from faker import Faker

fake = Faker()

"""Генерируем данные пользователя для регистрации"""
def generate_create_user_data():
    return {
        'email': f'user_{str(uuid.uuid4())[:8]}@test.com',
        'password': fake.password(length=10, special_chars=False),
        'name': fake.first_name()
    }
