# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.
n = int(input('введите число эн: '))
a = {}
for i in range(2*n+1):
    a[i] = i - n
print(a)
f = open('4task.txt')
p1 = int(f.readline())
p2 = int(f.readline())
print(a[p1]*a[p2])
