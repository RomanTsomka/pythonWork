#Задание 2.

"""Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк."""



time = int(input("Введите секунды: "))
time_resulthour = int(time // 3600)
time_resultminets = int(time // 60)
print(f"{time_resulthour}:{time_resultminets}:{time}")


