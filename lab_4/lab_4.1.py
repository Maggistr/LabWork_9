# Задание №1: Импортировать модуль math и использовать команду sqrt
import math
x = 0
while x == 0:
    try:


        number = float(input("Введите число: "))
        if number < 0:
            print("Нельзя извлечь корень из отрицательного числа.")
        else:
            print("Квадратный корень из вашего числа равен: " + str(math.sqrt(number)))
            break
    except ValueError:
        print("Введите лучше число.")




