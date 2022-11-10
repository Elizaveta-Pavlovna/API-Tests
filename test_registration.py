from register.api import Register
from register.models import RegisterUser
from schemas.registration import valid_schema
import pytest

URL = "https://stores-tests-api.herokuapp.com"

# задаем рандомные user, pass
# отпралвем запрос
# осуществляем необходимые проверки

class TestRegistration():
    def test_registration(self):
        body = RegisterUser.random()
        response = Register(url=URL).register_user(body=body, schema=valid_schema)
        assert response.status == 201
        assert response.response.get('message') == 'User created successfully.'
        assert response.response.get('uuid')