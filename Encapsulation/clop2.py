"""
В классе Hero из предыдущего занятия добавьте приватное свойство rank.
Создайте геттер, сеттер и делиттер чтобы можно было получить звание героя, установить звание "Победитель арены"
в случае победы героя в битве и удалить ранк в случае поражения.
"""


class Hero:
    def __init__(self, health, power, rank):
        self.health = health
        self.power = power
        self.__rank = rank

    def ranked(self, rank):
        self.__rank = rank

    def rankforclop(self):
        return self.__rank

    def forworstclop(self):
        del self.__rank

    def fight(self, enemy):
        while self.power > 0:
            enemy.health -= 77
            self.power -= 99
        if enemy.health < 0:
            self.ranked('Победитель Арены')
            print(self.rankforclop())
        else:
            self.forworstclop()
            print('Now, you`re worst clop...')


def now_fight():
    GigaClop = Hero(222, 333, 'Default')
    notaGigaClop = Hero(444, 1111, 'So so')
    GigaClop.fight(notaGigaClop)


now_fight()
