import requests

URL = ('https://dummyjson.com/users')
params = {'limit': 9999, 'skip': 0}
response = requests.get(url=URL, params=params)
users = response.json()["users"]
total_women = 0
for user in users:
    print(user)
for user in users:
    if user["gender"] == "female" and user["age"] < 30 and user["hair"]["color"] == "Brown":
        total_women += 1
for user in users:
    if user["gender"] == "male" and user["address"]["state"] == "Alabama":
        print(user["email"])
print(total_women)