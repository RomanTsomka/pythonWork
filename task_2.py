#Задание 2.

"""Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и только арифметические операции.
Не используйте взятие по индексу."""

a = int(input("Введите целое число: "))


# значение наибольшей цифры
max_digit = 0

# перебор цифр числа и сравнение с наибольшей
while num > 0:
    digit = num % 10
    if digit > max_digit:
        max_digit = digit
        if max_digit == 9:   
            break
    a //= 10

# вывод наибольшего числа
print(max_digit)




