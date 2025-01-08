#Сумма чисел
def sum(x, y):
    z = x + y
    print("Сумма ваших чисел: " + str(z))
#Произведение чисел
def prod(x, y):
    z = x * y
    print("Произведение ваших чисел: " + str(z))
#Деление чисел
def div(x, y):
    z = x / y
    print("Частное ваших чисел: " + str(z))
#Остаток от деления
def div_wth_remains(x, y):
    z = x % y
    print("Остаток деления ваших чисел: " + str(z))
#Разность чисел
def dif(x, y):
    z = x - y
    print("Разность ваших чисел: " + str(z))
#Большее число
def max(x, y):
    if x > y:
        print("Большее из ваших чисел: " + str(x))
    elif x == y:
        print("Числа равны.")
    else:
        print("Большее из ваших чисел: " + str(y))
#Меньшее число
def min(x, y):
    if x < y:
        print("Меньшее из ваших чисел: " + str(x))
    elif x == y:
        print("Числа равны.")
    else:
        print("Меньшее из ваших чисел: " + str(y))
#Возведение в степень
def pow(x, y):
    z = x ** y
    print(f'Ваше число {str(x)} в степени {str(y)} равно: {str(z)}')
#Квадратный корень из числа
def sqrt(z):
    import math
    x = 0
    while x == 0:
        if z >= 0:
            print(f"Квадратный корень из {str(z)} равен: {str(math.sqrt(z))}")
            break
        elif z < 0:
            print("Нельзя извлечь корень из отрицательного числа.")
            break




