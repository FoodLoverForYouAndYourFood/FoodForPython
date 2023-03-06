import os
os.mkdir(r"task")
f = open('answer.txt', 'w')
f.close()
os.replace('answer.txt', r'task\answer.txt')