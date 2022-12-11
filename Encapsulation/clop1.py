"""
Создайте класс банковского аккаунта по аналогии с примером из презентации. Сделайте атрибут name защищенным, а
balance и pasport приватными.
Добавьте геттер-методы на pasport и balance. Сделайте смену номера паспорта по поролю. А изменение баланса
на определенную сумму(сумма не может падать меньше 0, так что сделайте проверку).
Создайте метод удаляющий паспортные данные с аккаунта(также по поролю).
"""
class Account:

    def __init__(self, name, balance, passport, password):
        self._name = name
        self.__balance = balance
        self.__passport = passport
        self.__password = password

    def  clop1(self):
        return self.__balance

    def clop2(self, new_balance):
        self.__balance = new_balance

    def clop3(self):
        return self.__password

    def clop4(self):
        return self.__passport

    def clop5(self, new_passport, password):
        if password == self.get_password():
            self.__passport = new_passport
            print('успешно изменен')
        else:
            print('Не тот пароль')

    def clop6(self, password):
        if password == self.get_password():
            del self.__passport
            print('паспорт удален')
        else:
            print('Не тот пароль')

    def clop7(self, new):
        if self.__balance + new >= 0:
            self.__balance += new
            print(f'balance: {self.get_balance()}')
        else:
            print('Balance < 0 ')
