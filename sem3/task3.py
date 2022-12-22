# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу 
# между максимальным и минимальным значением 
# дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
import math
a = [1.1, 1.2, 3.1, 5, 10.01]
b = [b for b in range(len(a))]
for i in range(len(a)):
    b[i] = a[i] 
print(b)
for i in range(len(a)):
    if (a[i] - int(a[i])) == 0:
        b.pop(i)
print(b)
for i in range(len(b)):
    b[i] = b[i] - math.floor(b[i])
print(b)
print(max(b)-min(b))