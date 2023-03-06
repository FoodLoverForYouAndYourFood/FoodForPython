"""
Напишите 2 функции, одна считает сумму четных чисел, вторая нечетных
Запустите функции в разных процессах со значениями от 1 до c 100000
"""
import time
import multiprocessing
def task_Even(n = 100000):
    sum_Even = 0
    for i in range(n):
        if i % 2 == 0:
            sum_Even += i
            print(sum_Even)

def task_odd(n = 100000):
    sum_odd = 0
    for i in range(n):
        if i % 2 != 0:
            sum_odd += 1
            print(sum_odd)

def main():
    start = time.perf_counter()
    p1 = multiprocessing.Process(target=task_Even)
    p2 = multiprocessing.Process(target=task_odd)
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    finish = time.perf_counter()

if __name__ == 'main':
    main()