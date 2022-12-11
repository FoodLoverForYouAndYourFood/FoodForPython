"""
Создайте класс Person у которого будут свойства name и age.
Добавьте метод экземпляра который выводит информацию о человеке.
Создайте метод класса который генерирует новый объект класса
который ставить возраст человека: сегодняшний год - год который передают в метод.
(подсказка: тут можно использовать метод today().year класса date из модуля datetime)
Создайте статический метод который проверяет является ли совершеннолетним человек возраст которого передается в метод.
"""
from dateutil.utils import today


class GigaClop:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.name} {self.age}'

    def print_info(self):
        print(f'Имя: {self.name}\n'
              f'Возраст: {self.age}')

    @classmethod
    def create_gigaclop(cls, name, year):
        age = today().year - year
        return cls(name, age)

    @staticmethod
    def checkoclop(clop):
        if clop.age >= 18:
            return True
        else:
            return False


clop = GigaClop('Oleg', 20)
clop.print_info()

egor = GigaClop.create_gigaclop('Egor', 2007)
print(egor)

print(GigaClop.checkoclop(egor))
print(GigaClop.checkoclop(clop))



