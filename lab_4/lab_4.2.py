#Используйте модуль datetime для отображения текущей даты и времени
x = 0
while x == 0:
    import datetime

    agreement = input("Хотите ли вы узнать время ?").lower()
    if agreement == "y" or agreement == "yes" or agreement == "да" or agreement == "д":
        print(str(datetime.datetime.now()))
        break
    elif agreement == "n" or agreement == "no" or agreement == "н" or agreement == "нет" or agreement == "не":
        print("Как скажите.")
        break
    else:
        print("Дайте нормальный ответ.")
