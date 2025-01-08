def symbol():
    x = 0
    while x == 0:
        try:
            nums = int(input(print("Введите количество знаков которые вы хотите прочитать.")))
            file = open('../example_1.txt', encoding='utf-8')
            print(file.read(nums))
            file.close()
        except ValueError:
            print("Введите лучше число.")
def lines():
    x = 0
    while x == 0:
        try:
            nums = int(input(print("Введите количество строк которые вы хотите прочитать.")))
            file = open('../example_1.txt', encoding='utf-8')
            print(file.readline(nums))
            file.close()
        except ValueError:
            print("Введите лучше число.")
def all():
    admission = input(print("Хотите ли вы прочитать файл?(Y/N) "))
    if admission.lower() == "y":
        file = open('../example_1.txt', encoding='utf-8')
        print(file.read())
        file.close()
    else:
        print("Хорошо.")
def search():
    x = 0
    while x == 0:
        try:
            place = str(input('Введите имя файла: '))
            file = open(place + '.txt', 'r', encoding='utf-8')
            print(file.read())
            file.close()
            break
        except FileNotFoundError:
            print('Файл не был найден.Попробуйте ввести имя файла корректно.')
def write():
    x = 0
    while x == 0:
        user_input = str(input('Введите текст: '))
        file = open('../user_input_1.txt', 'a', encoding='utf-8')
        file.write(user_input)
        file = open('../user_input_1.txt', encoding='utf-8')
        print(file.read())
        break_point = str(input("Хотите ли вы остановить программу? "))
        if break_point.lower() == "да" or break_point.lower() == "д" or break_point.lower() == "yes" or break_point.lower() == "y":
            file.close()
            break

