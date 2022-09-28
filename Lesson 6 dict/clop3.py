#Напишите программу принимающую ввод информации о треке(место в чарте,исполнитель, название) пока пользовательне введет
# "off". Программа должна вывести всю информацию в виде словаря вида: {(место,испонитель): название трека}
a = {}
b = list()
while True:
    track = input('Трек: ')
    if track == 'off':
        break
    name = input('Имя: ')
    if name == 'off':
        break
    b.append(name)
    plase = input('Место: ')
    if plase == 'off':
        break
    b.append(plase)
    a[tuple(b)] = track
print(a)
