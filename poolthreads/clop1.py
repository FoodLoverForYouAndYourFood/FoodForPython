"""Отчисляем студентов в 2 раза быстрее.Создайте 2 функции для работы с очередью.В первой функции запросите пользователя вводить фамилии или off для завершения,добавьте фамилию в очередь.Во второй функции выводится сообщение что студент из очереди отчислен с фамилией студента.В основном потоке добавьте в очередь пару фамилий и запустите функции в разных потоках."""
from threading import Thread
from queue import Queue


def Impname(queue):
    while True:
        name = input()
        if name != 'off':
            queue.put(name)
        else:
            break

def Done(queue):
    while True:
        try:
            item = queue.get()
        except:
            continue
        else:
            print(f'Студент {item} БЫЛ ОТЧИСЛЕН')
            queue.task_done()


def main():
    queue = Queue()
    Impname_thread = Thread(target=Impname, args=(queue, ))
    Impname_thread.start()
    Done_thread = Thread(target=Done, args=(queue, ),daemon=True)
    Done_thread.start()
    Impname_thread.join()
    queue.join()

if __name__ == '__main__':
    main()