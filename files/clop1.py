"""
Напишите программу создающую .txt файл и записывающую туда строку "Я гений и стараюсь учить питон".
Выведите первые 7 символов файла на экран.
"""
with open('list.txt', 'w') as file:
    file.write('Один Один Два Два Три Один, Три, Четыре, Два, Два, Два, Два., Два')
    file.write('Один Один Два Два Три Один, Три, Четыре, Два, Два, Два, Два., Два')
with open('list.txt', 'r') as file:
    print(file.read(7))