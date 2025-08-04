import requests
import json

url = 'https://dummyjson.com/users'
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    with open('users.json', 'w', encoding='utf-8') as fl:
        json.dump(data, fl, ensure_ascii=False, indent=4)
    print("Данные были сохранены.")
else:
    print(f"Ошибка при запросе: {response.status_code}")