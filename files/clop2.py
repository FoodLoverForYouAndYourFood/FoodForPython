with open('list2.txt', 'w') as file1:
    file1.write('но у меня ничего не получается')
with open('list.txt', 'r') as file1:
    with open('list2.txt', 'a') as file:
        file.write(str(file1.read()))
with open('list2.txt', 'r') as file1:
    for line in file1:
        print(line)