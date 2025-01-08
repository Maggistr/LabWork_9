x = 0
while x == 0:
    try:
        number = int(input("Введите число: "))
        break
    except ValueError:
        print("Введите лучше число.")
def square(num_sq):
    print(f'Число в квадрате: {num_sq ** 2}')
square(number)







