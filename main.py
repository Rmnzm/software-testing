import requests

# payload = {"name": "User"}

# REDIRECTING 301 status code

# response = requests.post("https://playground.learnqa.ru/api/get_301", allow_redirects=True)
# first_response = response.history[0]
# second_response = response
# print(first_response.url)
# print(second_response.url)
#
# print(response.status_code)

# HEADERS
# headers = {"some_header": "123"} setUp USER headers
# response = requests.get("https://playground.learnqa.ru/api/show_all_headers", headers= headers)  improve headers
#
# print(response.text) in this you may see your headers
# print(response.headers)

# COOKIE (name, value, domain)

# payload = {"login":"secret_login", "password":"secret_pass"} - авторизация, установка кукис
# response1 = requests.post("https://playground.learnqa.ru/api/get_auth_cookie", data=payload) - запрос получения куки
#
# cookie_value = response1.cookies.get("auth_cookie") - сохренение куки в переменную
#
# cookies = {"auth_cookie": cookie_value}  - применение куки. создание словаря
#
# response2 = requests.post("https://playground.learnqa.ru/api/check_auth_cookie", cookies=cookies) - проверка авторизации с заданными уже куками
#
# print(response2.text) - текст ВЫ АВТОРИЗОВАНЫ
# print(response.status_code)
# print(dict(response.cookies))
#
# print(response.headers)


response1 = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params={"method": "GET"})
response2 = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method": "POST"})
response3 = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method": "PUT"})
response4 = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method": "DELETE"})
response5 = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type")
response6 = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method": "HEAD"})

methods = ["GET", "POST", "PUT", "DELETE"]
req = ["get", "post", "put", "delete"]

for method in methods:
    print((requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params={"method": method})).text)
    print((requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method": method})).text)
    print((requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method": method})).text)
    print((requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method": method})).text)



print(response1.text)
print(response2.text)
print(response3.text)
print(response4.text)
print(response5.text)
print(response6.text)