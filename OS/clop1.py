"""
Создайте программу выводящую информацию о системе вида:
Операционная система - ХХХ
Имя компьютера - ХХХ
Имя пользователя - ХХХ
"""
import os
print(os.environ.get('COMPUTERNAME'))
print(os.environ.get('HOMEPATH')[7:])
print(os.name)