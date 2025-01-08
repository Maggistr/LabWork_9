x = 0
while x == 0:
    try:
        number = int(input("Введите число: "))
        def is_prime(num):
            if num <= 1:
                return False
            for i in range(2, num):
                if num % i == 0:
                    return False
        if not is_prime(number):
            print("Число не простое.")
            break
        else:
            print("Число простое.")
            break
    except ValueError:
        print("Лучше введите число.")

