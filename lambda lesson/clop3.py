"""
Напишите список функций по требованию. Пользователь вводит имя.
Если имя заканчивается на А,Я,Г,М, то программа добавляет к имени "Гений".
Если на О,Ь,Л,Н. То добавляется "Сверхразум". Если ни на одну из этих букв то добавляется "Просто" перед именем.
"""
a = input('Введи имя, клоп:')
spisok = [lambda x: 'Гений ' + x, lambda x: 'Сверхразум ' + x, lambda x: 'Просто ' + x]
varA = ['а', 'я', 'г', 'м']
varB = ['о', 'ь', 'л', 'н']
if a[-1:] in varA:
    print(spisok[0](a))
if a[-1:] in varB:
    print(spisok[1](a))
if a[-1:] not in varA and a[-1:] not in varB:
    print(spisok[2](a))
