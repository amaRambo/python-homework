#  Создайте программу для игры в ""Крестики-нолики"". 
#  Игра реализуется в терминале, игроки ходят поочередно, 
#  необходимо вывести карту(как удобнее, можно например в виде списка, 
#  внутри которого будут 3 списка по 3 элемента, каждый из которого 
#  обозначает соответсвующие клетки от 1 до 9), сделать проверку не занята ли клетка,
#  на которую мы хотим поставить крестик или нолик, и проверку на победу
#  (стоят ли крестики или нолик в ряд по диагонали, вертикали, горизонтали)

matr = [ [1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

for i in range(len(matr)):
    for j in range(len(matr[i])):  
        print(matr[i][j], end=' ')
    print()

for count in range(1,10):
    p = "player X"
    print(p)
    pick = int(input("Сделайте ваш ход: "))
    if pick > 0 or pick < 10:
        for i in range(0,3):
            for j in range(0,3):
                if int(matr[i,j]) == pick:
                    strok = i
                    stolb = j
        matr[strok,stolb] = "X"
      

# import random
#
# maps = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# victories = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
#
#
# def check_victories():
#     for i in victories:
#         if maps[i[0]] == maps[i[1]] == maps[i[2]]:
#             return True
#         else:
#             return False
#
# def print_maps():
#     print(maps[0], end=" ")
#     print(maps[1], end=" ")
#     print(maps[2])
#
#     print(maps[3], end=" ")
#     print(maps[4], end=" ")
#     print(maps[5])
#
#     print(maps[6], end=" ")
#     print(maps[7], end=" ")
#     print(maps[8])
#
# print_maps()
# import random
#
# maps = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# victories = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
#
# name1 = input("Введите имя первого игрока - ")
# name2 = input("Введите имя второго игрока - ")
#
#
# first_turn = random.choice([name1,name2])
#
# print(first_turn)
# game_over = False
#
# cur_turn = first_turn
#
# while not game_over:
#     if cur_turn == first_turn:
#         symbol = "X"
#         step = int(input("введи клетку от 1 до 9, куда хочешь походить"))
#         if maps[int(step) - 1] == "X" or maps[int(step) - 1] == "0":
#             print("Occupied!!! Try Again")
#             continue
#         maps[step-1] = symbol

#     else:
#         symbol = "0"
#         step = int(input("введи клетку от 1 до 9, куда хочешь походить"))
#         if maps[int(step) - 1] == "X" or maps[int(step) - 1] == "0":
#             print("Occupied!!! Try Again")
#             continue
#         maps[step - 1] = symbol
#     print_maps()
#     if check_victories():
#         print(f"победил игрок {cur_turn}")
#         game_over = True
#     cur_turn = name2 if cur_turn == name1 else name1




