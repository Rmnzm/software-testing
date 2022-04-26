import json

string_as_json_format = '{"answer": "Hello, User"}'  # строка в формате json
obj = json.loads(string_as_json_format)  # parsing with json library

key = "answer2"

if key in obj:
    print(obj[key])
else:
    print(f"Ключа {key} в JSON нет")
