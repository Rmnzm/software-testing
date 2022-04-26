import requests

payload = {"name": "User"}

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
