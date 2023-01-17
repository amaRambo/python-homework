# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. 
# Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

import random

lottery = random.randint(1,2)
if lottery == 1:
    p = "player1"
else:
    p = "player2"

n = 2021
limit = 28
i = 0

while i <= n:
    print("Ход", p)
    step = int(input())
    while 0 <= step > 28 :
        print("Ваш ход неверный")
        print("Ход", p)
        step = int(input())
    i = i + step
    print("осталось конфет", n - i)
    if i == n:
        print(p, "Победил")
        break
    if p == "player1":
        p = "player2"
    else:
        p = "player1"
        




# import random
# while not 0<turn<max_sweet:

# def pve_s():
#     name1 = input("Введите имя первого игрока - ")
#     name2 = "bot"
#     sweets = int(input("Введите желаемое колчиество конфет - "))
#     max_sweet = int(input("Введите максимум конфет за ход"))
#
#     first_turn = random.choice([name1, name2])
#     flag = name1 if first_turn == name1 else name2
#
#     while sweets>0:
#         print(f"Ваш ход {flag}")
#
#         if flag == name1:
#             turn = int(input("введите желаемое количество конфет для взятия- "))
#
#             while not 0<turn<max_sweet:
#                 print("Введите конфеты в диапазоне от 0 до", max_sweet)
#                 turn = int(input("введите желаемое количество конфет для взятия- "))
#
#             sweets -= turn
#             if sweets>0:
#                 print(f'конфет осталось - {sweets}')
#             else:
#                 print(f'конфет осталось - 0')
#
#             flag = name2 if flag == name1 else name1
#         else:
#             turn = random.randint(1,max_sweet)
#             print(f"bot взял {turn} конфет")
#             sweets -= turn
#             if sweets > 0:
#                 print(f'конфет осталось - {sweets}')
#             else:
#                 print(f'конфет осталось - 0')
#
#             flag = name2 if flag == name1 else name1
#
#     winner = name2 if flag == name1 else name1
#     print(f"Поздравляем победил игрок {winner}")
#
#

# def pve_smart():
#     name1 = input("Введите имя первого игрока - ")
#     name2 = "bot"
#     sweets = int(input("Введите желаемое колчиество конфет - "))
#     max_sweet = int(input("Введите максимум конфет за ход"))
#
#     first_turn = random.choice([name1, name2])
#     flag = name1 if first_turn == name1 else name2
#
#     while sweets>0:
#         print(f"Ваш ход {flag}")
#
#         if flag == name1:
#             turn = int(input("введите желаемое количество конфет для взятия- "))
#
#         else:
#             if sweets == max_sweet:
#                 turn = sweets
#             elif sweets%max_sweet==0:
#                 turn = max_sweet-1
#             else:
#                 turn = sweets%max_sweet-1
#             print(f"bot взял {turn} конфет")
#             sweets -= turn
#             if sweets > 0:
#                 print(f'конфет осталось - {sweets}')
#             else:
#                 print(f'конфет осталось - 0')
#
#             flag = name2 if flag == name1 else name1
#
#     winner = name2 if flag == name1 else name1
#     print(f"Поздравляем победил игрок {winner}")
#
# pve_smart()
