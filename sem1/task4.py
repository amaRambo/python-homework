# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

a = int(input('введите номер четверти: '))
if a < 5 and a > 0:
    if a == 1:
        print("x > 0, y > 0")
    if a == 2:
        print("x < 0, y > 0")
    if a == 3:
        print("x < 0, y < 0")
    if a == 4:
        print("x > 0, y < 0")
else:
    print("неверно введена четверть")