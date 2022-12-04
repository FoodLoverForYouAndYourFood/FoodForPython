"""
Создайте класс SpaceObject у которого будут свойство размер.
Создайте 2 класса Star и Planet которые будут наследовать SpaceObject. В классе Star добавьте свойство яркость
и метод светить в котором будет выводится на экран с какой яркостью светит звезда.
Классу Planet добавьте свойства население и прирост за год и метод который будет печатать население через переданное
ему количество лет.
"""


class SpaceObject:
    def __init__(self, size):
        self.size = size


class Star(SpaceObject):
    def __init__(self, size, brightness):
        self.brightness = brightness
        super().__init__(size)

    def bright(self):
        print( f'Звезда светит с яркостью:{self.brightness} ')


class Planet(SpaceObject):
    def __init__(self, size, numcreature, numplus):
        self.numplus = numplus
        self.numcreature = numcreature
        super().__init__(size)

    def all_people(self):
        n = int(input('Введите количество лет,через которое хотите узнать количество существ на планете:'))
        print(f'Количество существ на планете через', n, 'лет равно', int(self.numcreature) + int(self.numplus) * n)


Star('8598239297229km^3',450000).bright()
Planet('38998328782498km^3', 1000000, 1000).all_people()