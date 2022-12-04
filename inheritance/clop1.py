"""
Добавьте на основании классов из презентации класс Magician который наследует Hero. Со своими методами hello и atack.
"""


class Hero:
    def __init__(self, HP, armor, equipment, weapon, strength, name):
        self.HP = HP
        self.strength = strength
        self.armor = armor
        self.name = name
        self.weapon = weapon
        self.equipment = equipment

    def info(self):
        print('' + str(self.name) + '')
        print('HP->', self.HP)
        print('Armor->', self.armor)
        print('Weapon->', self.weapon)
        print('Equipment->', self.equipment)


class Magician(Hero):
    def __init__(self, mana, skills, HP, armor, equipment, weapon, strength, name):
        self.mana = mana
        self.skills = skills
        super().__init__(HP, armor, equipment, weapon, strength, name)

    def additionally(self):
        print('Skills->', self.skills)
        print('Mans->', self.mana)

    def hello(self):
        print('Начинающий маг отправиться в путешествие отсюда, встречайте!')

    def fight(self, enemy):
        if enemy.armor >= self.strength:
            enemy.armor -= self.strength
        if self.strength > enemy.armor > 0:
            enemy.armor -= self.strength
            enemy.HP += enemy.armor
        elif enemy.armor <= 0:
            enemy.HP -= self.strength


George = Magician(100, 'fire arrow', 50, 20, 'old_backpack', 'stick', 10, 'George')
George.hello()
George.info()