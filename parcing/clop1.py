"""
Соберите данные с чартов яндекс музыки https://music.yandex.ru/chart
Внимательно изучите источник, посмотрите как именно на сайт приходит информация.
Сохраните данные в json файл в формате:
{
место в чарте: (исполнитель,трек)
}
"""
import json

import requests
from bs4 import BeautifulSoup
import lxml

k = 0
lst_song = []
lst_name = []
slovar = {}
with open("yandex.html", "r", encoding="UTF-8") as file:
    page = file.read()
    bs = BeautifulSoup(page, "lxml")
    containers = bs.find_all("div", "d-track__name")
    for i in containers:
        k += 1
        song = i.find("a", "d-track__title deco-link deco-link_stronger")
        try:
            lst_song.append(song.text)
        except:
            pass

    container1 = bs.find_all("span", "d-track__artists")
    for j in container1:
        name = j.find("a", "deco-link deco-link_muted")
        try:
            lst_name.append(name.text)
        except:
            pass
for i in range(k - 1):
    slovar[i + 1] = str(str(lst_name[i]) + ' , ' + str(lst_song[i]))
print(slovar)
with open('file.json', 'w', encoding='UTF-8') as f:
    json.dump(slovar, f, indent=4, ensure_ascii=False)