import requests
import time
import json

response_1 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job") # Запрос на получение токена

response_1_text = response_1.text
response_json = json.loads(response_1_text) # Парсинг текста ответа в json
token = response_json["token"] # Получение токена из ответа


response_2 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token": token}) # Запрос с токеном, на создание задачи и статуса по задаче

response_2_json = json.loads(response_2.text) # Парсинг ответа в json
print(response_2_json)
time.sleep(10) #

response_3 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token": token}) # Запрос с токеном, после завершения задачи на получение результата

response_3_json = json.loads(response_3.text) # Парсинг ответа в json
print(response_3_json)


# Вывод результатов. В зависимости от того, присутствует ли поле result и выполнена ли задача.
if response_3_json["result"] is not None and response_3_json["status"] == "Job is ready":
    print(True)
else:
    print(False)