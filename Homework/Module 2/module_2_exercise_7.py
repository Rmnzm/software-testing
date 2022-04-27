import requests

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