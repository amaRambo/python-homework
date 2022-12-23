# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10
def dvoich(num, result = ""):
  if num == 0:
    return result[::-1]
  result += str(num%2)
  return dvoich(num//2,result)
n = int(input())
if n!=0:
  print(dvoich(n))
else:
  print(0)
