import requests
from bs4 import BeautifulSoup

print(f"Версія Requests: {requests.__version__}")

# Виконуємо HTTP-запит
response = requests.get('https://www.google.com')

# Парсимо HTML-код
soup = BeautifulSoup(response.text, 'html.parser')
title = soup.find('title').text

print(f"Заголовок сторінки: {title}")