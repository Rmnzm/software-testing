from json.decoder import JSONDecodeError
import requests

# response = requests.get('https://playground.learnqa.ru/api/get_text', params={"param1":1})
#
#
# try:
#     parsed_response_json = response.json()
#     print(parsed_response_json)
# except JSONDecodeError:
#     print("Invalid format")

response = requests.post("https://playground.learnqa.ru/api/check_type", data={"param": "param"})
print(response.text)

