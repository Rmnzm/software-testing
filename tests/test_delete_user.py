from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.my_requests import MyRequests


class TestDeleteUser(BaseCase):
    def test_delete_user_id_2(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }

        response_login = MyRequests.post(
            "/user/login",
            data=data
        )

        auth_sid = self.get_cookie(response_login, "auth_sid")
        token = self.get_header(response_login, "x-csrf-token")

        response_delete = MyRequests.delete("/user/2", headers={"x-csrf-token": token},
                                            cookies={"auth_sid": auth_sid})

        Assertions.assert_code_status(response_delete, 400)
        assert response_delete.content.decode('utf-8') == "Please, do not delete test users with ID 1, 2, 3, 4 or 5."

    def test_delete_user(self):
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

        # DELETE
        response_delete = MyRequests.delete(f"/user/{user_id}", headers={"x-csrf-token": token},
                                            cookies={"auth_sid": auth_sid})

        Assertions.assert_code_status(response_delete, 200)

        # GET DELETED USER
        response_get_deleted_user = MyRequests.get(f"/user/{user_id}")

        Assertions.assert_code_status(response_get_deleted_user, 404)
        assert response_get_deleted_user.content.decode('utf-8') == "User not found"

    def test_delete_user_from_another_user_auth(self):
        # REGISTER
        register_data = self.prepare_registration_user()
        response_resister = MyRequests.post("/user/", data=register_data)

        Assertions.assert_code_status(response_resister, 200)
        Assertions.assert_json_has_key(response_resister, "id")
        user_id = self.get_json_value(response_resister, "id")

        # LOGIN
        login_data = {
            "email": "vinkotov@example.com",
            "password": "1234"
        }
        response_login = MyRequests.post("/user/login", data=login_data)

        auth_sid = self.get_cookie(response_login, "auth_sid")
        token = self.get_header(response_login, "x-csrf-token")

        # DELETE
        response_delete = MyRequests.delete(f"/user/{user_id}", headers={"x-csrf-token": token},
                                            cookies={"auth_sid": auth_sid})

        Assertions.assert_code_status(response_delete, 400)
        assert response_delete.content.decode('utf-8') == "Please, do not delete test users with ID 1, 2, 3, 4 or 5."
