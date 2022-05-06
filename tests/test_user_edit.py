import allure

from lib.my_requests import MyRequests
from lib.assertions import Assertions
from lib.base_case import BaseCase


@allure.epic("Изменение данных пользователя")
class TestUserEdit(BaseCase):
    @allure.testcase("Изменение данных авторизованного пользователя")
    def test_edit_just_created_user(self):
        # REGISTER
        register_data = self.prepare_registration_user()
        response_resister = MyRequests.post("/user/", data=register_data)

        Assertions.assert_code_status(response_resister, 200)
        Assertions.assert_json_has_key(response_resister, "id")

        email = register_data["email"]
        first_name = register_data["firstName"]
        password = register_data["password"]
        user_id = self.get_json_value(response_resister, "id")

        # LOGIN
        login_data = {
            "email": email,
            "password": password
        }
        response_login = MyRequests.post("/user/login", data=login_data)

        auth_sid = self.get_cookie(response_login, "auth_sid")
        token = self.get_header(response_login, "x-csrf-token")

        # EDIT
        new_name = "Changed Name"

        response_edit = MyRequests.put(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
            data={"firstName": new_name}
        )

        Assertions.assert_code_status(response_edit, 200)

        # GET
        response_get_changed_user = MyRequests.get(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )

        Assertions.assert_json_value_by_name(
            response_get_changed_user,
            "firstName",
            new_name,
            "Wrong name of the user after edit"
        )

    @allure.testcase("Неудачное изменение неавторизованного пользователя")
    def test_edit_user_from_unauthorised_user(self):
        new_name = "Changed Name"

        response_edit = MyRequests.put(
            "/user/2",
            data={"firstName": new_name}
        )

        Assertions.assert_code_status(response_edit, 400)
        assert response_edit.content.decode('utf-8') == "Auth token not supplied"

    @allure.testcase("Неудачное изменение email пользователю")
    def test_edit_user_email_to_incorrect_email(self):
        register_data = self.prepare_registration_user()
        response_resister = MyRequests.post("/user/", data=register_data)

        Assertions.assert_code_status(response_resister, 200)
        Assertions.assert_json_has_key(response_resister, "id")

        email = register_data["email"]
        password = register_data["password"]
        user_id = self.get_json_value(response_resister, "id")

        # LOGIN
        login_data = {
            "email": email,
            "password": password
        }
        response_login = MyRequests.post("/user/login", data=login_data)

        auth_sid = self.get_cookie(response_login, "auth_sid")
        token = self.get_header(response_login, "x-csrf-token")

        new_email = "email example.com"

        response_edit = MyRequests.put(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
            data={"email": new_email}
        )

        Assertions.assert_code_status(response_edit, 400)
        assert response_edit.content.decode('utf-8') == "Invalid email format"

    @allure.testcase("Неудачное изменение данных пользователя с авторизацией под другим пользователем")
    def test_edit_user_from_auth_another_user(self):
        data_user_edit = self.prepare_registration_user()

        response_user_edit = MyRequests.post("/user/", data=data_user_edit)

        Assertions.assert_code_status(response_user_edit, 200)
        Assertions.assert_json_has_key(response_user_edit, "id")
        user_id = response_user_edit.json()["id"]

        response1 = MyRequests.post("/user/login", data={
            "email": "vinkotov@example.com",
            "password": "1234"
        })

        auth_sid = self.get_cookie(response1, "auth_sid")
        token = self.get_header(response1, "x-csrf-token")

        new_name = "Changed Name"

        response_edit = MyRequests.put(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
            data={"firstName": new_name}
        )

        Assertions.assert_code_status(response_edit, 400)
        assert response_edit.content.decode('utf-8') == "Please, do not edit test users with ID 1, 2, 3, 4 or 5."

    @allure.testcase("Неудачное изменение username на короткий username")
    def test_edit_username_to_shortest_name(self):
        # REGISTER
        register_data = self.prepare_registration_user()
        response_resister = MyRequests.post("/user/", data=register_data)

        Assertions.assert_code_status(response_resister, 200)
        Assertions.assert_json_has_key(response_resister, "id")

        email = register_data["email"]
        first_name = register_data["firstName"]
        password = register_data["password"]
        user_id = self.get_json_value(response_resister, "id")

        # LOGIN
        login_data = {
            "email": email,
            "password": password
        }
        response_login = MyRequests.post("/user/login", data=login_data)

        auth_sid = self.get_cookie(response_login, "auth_sid")
        token = self.get_header(response_login, "x-csrf-token")

        # EDIT
        new_name = "a"

        response_edit = MyRequests.put(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
            data={"firstName": new_name}
        )

        Assertions.assert_code_status(response_edit, 400)
        assert response_edit.json()["error"] == "Too short value for field firstName"
