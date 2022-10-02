# Каждая семья, живущая в доме N, выписывает газету, или журнал, или и то, и другое.
# 75 семей выписывают газету, 27 - журнал, 13 - и журнал, и газету.
# Даны списки семей в квартирах.
# Используя операции со множествами вычислите сколько семей живёт в доме N.
newspaper = set(range(1, 76))
magazine = set(range(77, 104))
both = set(range(21, 34))
f = newspaper | magazine - both
print(len(f))