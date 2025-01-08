x = 0
while x == 0:
    try:
        a = int(input("Введите первое число: "))
        b = int(input("Введите второе число: "))
        def max_of_two(x, y):
            if x > y:
                print("Большее число: " + str(x))
            elif x < y:
                print("Большее число: " + str(y))
            else:
                print("Числа равны.")
        break
    except ValueError:
        print("Введите лучше число.")
max_of_two(a, b)

