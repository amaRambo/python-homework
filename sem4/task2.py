# Задайте натуральное число N. Напишите программу,
#  которая составит список простых множителей числа N.

n = int(input("n="))
lst = []
lst2 = []
for i in range(2, n+1):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        lst.append(i)
for i in range(2, len(lst)):
    if n % lst[i] == 0:
        lst2.append(i)
print(lst)
print(lst2)

