# Напишите программу, которая на вход принимает два числа A и B,
#  и возводит число А в целую степень B с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

a = 3
b = 5
def power(a,b):
    if b == 1:
        return a
    else:
        return power(a,b-1)*a
print(power(a,b))