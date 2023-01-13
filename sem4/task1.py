# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

a = 0.001
n = 0
с = 3 + 1/7
while a%1 != 0:
    n += 1
    a = a * 10
template = '{:.' + str(n) + 'f}'
print(template.format(с))

# import math
# n = input()
# length = len(n.split(".")[1])
# print(round(math.pi,length))
