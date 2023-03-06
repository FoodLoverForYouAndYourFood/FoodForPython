"""
Создайте функцию которая выводит на экран все делители числа.
Создайте очередь и добавьте в нее числа.
Создайте пул потоков и запустите в пуле функцию с очередью.
"""
from threading import Thread
from queue import Queue


def ImportNums(queue):
    while True:
        Lstnums = input()
        if Lstnums != 'off':
            Lstnums = Lstnums.split(' ')
            queue.put(Lstnums)
        else:
            break
def takeDiv(queue):
    while True:
        try:
            Nums = queue.get()
        except:
            continue
        else:
            for i in range(len(Nums)):
                for j in range(2, int(Nums[i])):
                    if int(Nums[i]) % j == 0:
                        print(f'Делитель {Nums[i]} -', j)
            queue.task_done()


def main():
    queue = Queue()
    Impname_thread = Thread(target=ImportNums, args=(queue, ))
    Impname_thread.start()
    Done_thread = Thread(target=takeDiv, args=(queue, ),daemon=True)
    Done_thread.start()
    Impname_thread.join()
    queue.join()

if __name__ == '__main__':
    main()