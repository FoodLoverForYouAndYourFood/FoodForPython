def main(inputin):
    if 'расп' in inputin.lower():
        timetable()
    if 'трен' in inputin.lower():
        coach()
    if 'цена' in inputin.lower():
        cost()
    if 'инфо' or 'сайт' in inputin.lower():
        info_and_site()


def timetable():
    print('Пон с 12:30 до 20:00\nВтор с 11:30 до 20:00\nСред с 10:30 до 20:00\nЧет с 10:30 до 20:00\nПят с 10:30 до 19:00\n')



def coach():
    print('Филипов Егор aka Повелитель пива\nP.S Пока единственный тренер по правильному выпиванию пива, зато какой!!!')


def cost():
    print('С вас 3 ящика пива \n никнейм в дискорде\n 3 тысячи ммр в Доте \n сборник анекдотов или хотя бы знание больше 10 штук')


def info_and_site():
    print('Пивной gym \n Тут тебя подтянут и натянут\n DotaBeerForClops.net')