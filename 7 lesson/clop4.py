first = "0 0 0 0 0 0 0"  # Вывод должен быть 0
second = "1 1 1 0 0 0 0"  # Вывод должен быть 3
third = "1 1 1 1 1 1 1"  # Вывод должен быть 1
A, B, C, D, E, F, G = map(int, first.split())
print(A + B + C - F + D + E - G)
A, B, C, D, E, F, G = map(int, second.split())
print(A + B + C - F + D + E - G)
A, B, C, D, E, F, G = map(int, third.split())
print(A + B + C - (F + D + E - G))