"""
Напишите функцию cacluate, которая может принимать любое количество чисел и возвращать кортеж.
Первое значение кортежа - это среднее значение всех параметров, а второе значение - все числа, превышающие среднее значение.
Второе значение оформите в виде списка.
"""


def main():
    cacluate()


def Sr(A):
    Sum = 0
    for i in range(len(A)):
        Sum += A[i]
    return Sum / len(A)


def cacluate():
    lst = []
    newlts = []
    while True:
        a = input()
        if a == '':
            break
        else:
            lst.append(float(a))
    for i in range(len(lst)):
        if Sr(lst) < lst[i]:
            newlts.append(lst[i])
    cortLST = (Sr(lst), newlts)
    cort = tuple(cortLST)
    print(cort)


main()
