"""
Напишите программу-имитатор подбрасывания 2 кубиков.
Программа выводит на экран "подбрасываю кубики" и спустя 2 секунды выводит значения на кубиках в одну строку.
"""
from random import *
from time import *
K1 = randint(0, 6)
K2 = randint(0, 6)
print('Подбрасываю кубики')
sleep(2)
print(K1, K2)