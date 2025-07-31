from pprint import pprint
import requests

URL = ('https://dummyjson.com/todos')
params = {'limit': 450, 'skip': 0}

response = requests.get(url=URL, params=params)


response_json = response.json()
# pprint(response_json)
todos = response_json['todos']
# pprint(todos)

uncompl = 0
film_related_todos = []
key_word = 'diy'
for todo in todos:
    # {'id': 253, 'todo': 'Try a new fitness class like aerial yoga or barre', 'completed': True, 'userId': 21}
    print(todo)
    if not todo['completed']:
        uncompl += 1
    if key_word in todo['todo'].lower():
        film_related_todos.append(todo['todo'])

print(f'{uncompl=}')
print(f'{film_related_todos=}')