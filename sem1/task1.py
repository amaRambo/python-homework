# Напишите программу, которая принимает на вход цифру,
# обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет

a = int(input('ВВедите день недели: '))
if a > 7 or a < 1:
    print("Нет такого дня недели")
else:
    if a == 6 or a == 7:
        print("сегодня выходной")
    else:
        print("иди работай, дядя))")