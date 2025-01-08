while True:
    try:
        num_1 = int(input("Введите первое число:"))
        num_2 = int(input("Введите второе число:"))
        break
    except ValueError:
        print('Введите лучше число.')
def max_of_nums(num_1,num_2):
    if num_2 < num_1:
        print("Большее число: " + str(num_1))
    elif num_2 == num_1:
        print("Числа равны.")
    else:
        print("Большее число: " + str(num_2))


max_of_nums(num_1, num_2)