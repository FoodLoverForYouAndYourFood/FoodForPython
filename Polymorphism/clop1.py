"""
Создайте классы утка и человек. У обоих классов нету свойств, но есть методы крякать и носить одежду.
Утка крякает, а человек имитирует кряканье. Добавьте экземпляры этих классов в список и вызовите в цикле соответствующие методы.
"""


class Gigachad:

    def imitation(self):
        print('А мужик то реально крякнул...')

    def gucci_for_all(self):
        print('Гигачад решил одеться, всем встать!')


class Duck:

    def imitation(self):
        print('*что-то на крякающем(кто понял,тот понял(утка поняла, я думаю))*')

    def gucci_for_all(self):
        print('Оно оделось....')


def main():
    my_list = [Gigachad(), Duck()]
    for i in my_list:
        i.imitation()
        i.gucci_for_all()


main()
