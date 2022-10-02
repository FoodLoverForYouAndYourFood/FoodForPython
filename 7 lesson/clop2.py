# Имеется список с произвольными значениями. Нужно преобразовать его во множество и проверить
# являются ли все его элементы неизменяемыми.
# Вывести True или False. И изменяемые элементы
# Подсказка: чтобы узнать тип элемента можно использовать функцию type()
testList = [1, 2, 2, [3, 4], (1, 2, 3), "1", {1, 2, 3}]
printSet = set()
for i in testList:
    if type(i) == list or type(i) == dict or type(i) == set:
        testList.remove(i)
    else:
        printSet.add(i)
if len(printSet) > 0:
    print(True)
    print(testList)
else:
    print(False)
