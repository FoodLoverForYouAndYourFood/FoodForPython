# Создайте словарь с количеством элементов не менее 5-ти.
# Поменяйте местами первый и последний элемент объекта.
# Удалите второй элемент. Добавьте в конец ключ «new_key» со значением «new_value».
# Выведите на печать итоговый словарь. Важно, чтобы словарь остался тем же (имел тот же адрес в памяти).
dict1 = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5}
dict1['1'], dict1['5'] = dict1['5'], dict1['1']
del dict1['2']
dict1['new_key'] = 'new_value'
print(dict1)
