"""
Создайте функцию напоминалку в отдельном потоке от основном программы.
Функция должна запрашивать о чем напомнить и через сколько секунд.
В основной части программы запустите поток с функцией и выполните задержку в 10 секунд.
После выполнения программа должна написать "программа завершается"
"""
from threading import Thread
import time
def tip():
    f = input('О чём напомнить?')
    s = input('Через сколько времени?')
    time.sleep((int(s)))
    print(f)
t1 = Thread(target=tip(),name=None,args=())
t1.start()
t1.join()
time.sleep(10)
print('Основной поток завершён')