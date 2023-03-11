"""
Изучите API сервиса https://randomuser.me/
Выведите цитату "Hi, im #NAME, im from #COUNTRY, my phone number is #PHONE"
"""
import requests
import json
from bs4 import BeautifulSoup
url = ('https://randomuser.me/api/')
a = requests.get(url)
with open('file.json', 'w', encoding='UTF-8') as f:
    f.write(a.text)
with open('file.json', 'r', encoding='UTF-8') as f:
    data = json.load(f)
print('Hello  im ' + data['results'][0]['name']['first'] + ' im from ' + data['results'][0]['location']['country'] + 'my phone number ' + data['results'][0]['phone'])