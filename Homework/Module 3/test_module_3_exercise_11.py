import requests


class TestResolveCookie:
    def test_resolve_cookie(self):
        response = requests.get("https://playground.learnqa.ru/api/homework_cookie")

        cookie = response.cookies.get("HomeWork")

        print(cookie)

        assert cookie == "hw_value", f"Cookie is not equal 'hw_value'"
