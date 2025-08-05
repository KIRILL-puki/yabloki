import requests

URL = ('https://dummyjson.com/carts')
params = {'limit': 9999, 'skip': 0}
response = requests.get(url=URL, params=params)
carts = response.json()["carts"]

total = 0
for cart in carts:
    if cart["userId"] <= 25:
        total += cart["total"]

print(f"Price: {total}")