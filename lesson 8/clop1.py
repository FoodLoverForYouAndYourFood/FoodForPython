"""
Напишите программу печатающую бейджики учеников.
Программа запрашивает ввод числа учеников и печатает каждому бейджик. Бейдж содержит название учебного заведения:
«Колледж Сириус», поле для имени:
«Имя: ____» и поле для школы:
«Группа: ____». Напиши программу, печатающую бейджики студентов как на картинке. В завершении программа должна печатать:
«Готово! Заберите бейджики.»
Функция должна принимать имя и группу ученика.
"""


def print_visitka():
    print('Колледж Сириус')
    print('Имя:', g)
    print('Группа:', n)


students = int(input())
for i in range(students):
    g = input('Имя:')
    n = input('Группа:')
    print_visitka()
print('Готово! Заберите бейджики.')
