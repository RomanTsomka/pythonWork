#Задание 3.

"""Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn."""

a_integer = int(input("Введите целое положительное число: "))
if a_integer >= 0:
    print(f"{a_integer + (a_integer * a_integer) + (a_integer * a_integer * a_integer)}")
else:
    print("Число не положительное")