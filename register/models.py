# register/models
from faker import Faker

fake = Faker()

#функция random генерирует каждый раз рандомные данные
class RegisterUser:
    @staticmethod
    def random():
        username = fake.email()
        password = fake.password()
        return {"username": username, "password": password}


# Если мы поменяем requests, то нам необходимо будет менять все тесты, так как новая библиотека может не иметь
# атрибут status_code и метод json(), которые принадлежат библиотеке requests. Будем править, добавим в models:
class ResponseModel:
    def __init__(self, status: int, response: dict = None):
        self.status = status
        self.response = response