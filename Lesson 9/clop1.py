"""
Создайте функцию которая принимает на вход 3 именованных параметра, выведите на печать значения этих параметров,
но только в том случае если они не равны None.
"""


def ur_mom():
    A = input()
    B = input()
    C = input()
    if A != B != C != 'None':
        print(A, B, C)


ur_mom()
