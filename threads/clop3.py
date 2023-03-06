"""
Создайте функцию в демоне потока которая каждые 3 секунды будет писать "Вводите быстрее".
В основной части программы запросите ввод кода от бомбы и если код неверный выведите: "Вы взорвались", если верный - "Бомба разминирована"
"""
from threading import Thread
import time
def qwerty():
    while True:
        time.sleep(5)
        print('\n')
        print('Пиши, не задерживайся')
d = Thread(target=qwerty,daemon=True)
d.start()

code = 123456
c =int(input('Введите код'))
print()
if c == code:
    print('ВАУ,малыш, а ты вовремя)')
else:
    print('Мда,мальчик мой не успел, ты проиграл')