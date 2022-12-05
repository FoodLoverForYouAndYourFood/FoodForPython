"""
Создайте класс который будет устанавливать свойство name и иметь метод
который к имени прибавляет надпись "гений". Создайте еще 1 класс, унаследуйте предыдущий.
Во втором классе вызовите метод класса родителя и добавьте к выводу надпись "но его отчислят если он не будет учить ООП".
Создайте экземпляр второго класса с вашим именем и вызовите метод печатающий всю надпись.
"""


class Clop1:

    def __init__(self, name):
        self.name = name

    def forgenius(self):
        return f'{self.name} гений'


class Clop2(Clop1):

    def __init__(self, name):
        super().__init__(name)

    def make_object(self):
        nick = Clop1(self.name)
        return nick

    def complete(self):
        print(f'{self.make_object().forgenius()}, но его отчислят если он не будет учить ООП')


david = Clop2("David")
david.complete()