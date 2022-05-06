import pytest

from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.my_requests import MyRequests


class TestUserRegister(BaseCase):
    exclude_params = [
        ('no_password'),
        ('no_username'),
        ('no_firstName'),
        ('no_lastName'),
        ('no_email')
    ]

    def test_create_new_user(self):
        data = self.prepare_registration_user()

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response, "id")

    def test_create_user_with_existing_email(self):
        email = "vinkotov@example.com"
        data = self.prepare_registration_user(email)

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode(
            'utf-8') == f"Users with email '{email}' already exists", f"Unexpected response content {response.content}"

    def test_create_user_with_incorrect_email(self):
        email = "vinkotov example.com"
        data = self.prepare_registration_user(email)

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode('utf-8') == "Invalid email format", "Incorrect request. Please try to change " \
                                                                           "your request "

    @pytest.mark.parametrize("condition", exclude_params)
    def test_create_email_without_some_params(self, condition):

        if condition == "no_password":
            data = {
                "username": "learnqa",
                "firstName": "learnqa",
                "lastName": "learnqa",
                "email": "vinkotov@example.com"
            }
            response = MyRequests.post("/user/", data=data)
            Assertions.assert_code_status(response, 400)
            assert response.content.decode('utf-8') == "The following required params are missed: password"

        if condition == "no_username":
            data = {
                "password": "123",
                "firstName": "learnqa",
                "lastName": "learnqa",
                "email": "vinkotov@example.com"
            }
            response = MyRequests.post("/user/", data=data)
            Assertions.assert_code_status(response, 400)
            assert response.content.decode('utf-8') == "The following required params are missed: username"

        if condition == "no_firstName":
            data = {
                "password": "123",
                "username": "learnqa",
                "lastName": "learnqa",
                "email": "vinkotov@example.com"
            }
            response = MyRequests.post("/user/", data=data)
            Assertions.assert_code_status(response, 400)
            assert response.content.decode('utf-8') == "The following required params are missed: firstName"

        if condition == "no_lastName":
            data = {
                "password": "123",
                "username": "learnqa",
                "firstName": "learnqa",
                "email": "vinkotov@example.com"
            }
            response = MyRequests.post("/user/", data=data)
            Assertions.assert_code_status(response, 400)
            assert response.content.decode('utf-8') == "The following required params are missed: lastName"

        if condition == "no_email":
            data = {
                "password": "123",
                "username": "learnqa",
                "firstName": "learnqa",
                "lastName": "learnqa"
            }
            response = MyRequests.post("/user/", data=data)
            Assertions.assert_code_status(response, 400)
            assert response.content.decode('utf-8') == "The following required params are missed: email"

    def test_create_user_with_shortest_username(self):
        data = {
            "password": "123",
            "username": "l",
            "firstName": "learnqa",
            "lastName": "learnqa",
            "email": "vinkotov@example.com"
        }
        response = MyRequests.post("/user/", data=data)
        Assertions.assert_code_status(response, 400)
        assert response.content.decode('utf-8') == "The value of 'username' field is too short"

    def test_create_user_with_longest_username(self):
        data = {
            "password": "123",
            "username": "a" * 251,
            "firstName": "learnqa",
            "lastName": "learnqa",
            "email": "vinkotov@example.com"
        }
        response = MyRequests.post("/user/", data=data)
        Assertions.assert_code_status(response, 400)
        assert response.content.decode('utf-8') == "The value of 'username' field is too long"
