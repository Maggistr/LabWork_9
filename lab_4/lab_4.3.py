#Создать свой модуль импортировать его(MyModule_1.py)
def deystviye(deystviye):
    if deystviye == "+" or deystviye == "-" or deystviye == "%" or deystviye == "/" or deystviye == ">" or deystviye == "<" or deystviye == "**" or deystviye == "**0,5" or deystviye == "*":
        return True
    if deystviye != "+" or deystviye != "-" or deystviye != "%" or deystviye != "/" or deystviye != ">" or deystviye != "<" or deystviye != "**" or deystviye != "**0,5" or deystviye == "*":
        return False
def soglasie(soglasie):
    if soglasie.lower() == "y":
        return True
    if soglasie.lower() == "n":
        return False
print("ПОДСКАЗКА ПО ЗНАКАМ:\n+СУММА\n-РАЗНОСТЬ\n*ПРОИЗВЕДЕНИЕ\n/ЧАСТНОСТЬ\n%ОСТАТОК ОТ ДЕЛЕНИЯ\n**ВОЗВЕДЕНИЕ В СТЕПЕНЬ\n**0.5КВАДРАТНЫЙ КОРЕНЬ\n>БОЛЬШЕЕ\n<МЕНЬШЕЕ")
import MyModule

x = 0
while x == 0:
    c = input("Какое действие вы хотите выполнить:\n(Введите только знак.)")
    if deystviye(c) == True:
        if c == "+":
            a = int(input("Введите первое число: "))
            b = int(input("Введите второе число: "))
            MyModule.sum(a, b)
            admission = input("Хотите ли вы завершить программу?(Y/N)")
            if soglasie(admission.lower()) == True:
                break
        if c == "-":
            a = int(input("Введите первое число: "))
            b = int(input("Введите второе число: "))
            MyModule.dif(a, b)
            admission = input("Хотите ли вы завершить программу?(Y/N)")
            if soglasie(admission.lower()) == True:
                break
        if c == "*":
            a = int(input("Введите первое число: "))
            b = int(input("Введите второе число: "))
            MyModule.prod(a, b)
            admission = input("Хотите ли вы завершить программу?(Y/N)")
            if soglasie(admission.lower()) == True:
                break
        if c == "**":
            a = int(input("Введите первое число: "))
            b = int(input("Введите степень: "))
            MyModule.pow(a, b)
            admission = input("Хотите ли вы завершить программу?(Y/N)")
            if soglasie(admission.lower()) == True:
                break
        if c == "**0,5":
            a = int(input("Введите ваше число: "))
            MyModule.sqrt(a)
            admission = input("Хотите ли вы завершить программу?(Y/N)")
            if soglasie(admission.lower()) == True:
                break
        if c == "/":
            a = int(input("Введите первое число: "))
            b = int(input("Введите второе число: "))
            MyModule.div(a, b)
            admission = input("Хотите ли вы завершить программу?(Y/N)")
            if soglasie(admission.lower()) == True:
                break
        if c == "%":
            a = int(input("Введите первое число: "))
            b = int(input("Введите второе число: "))
            MyModule.div_wth_remains(a, b)
            admission = input("Хотите ли вы завершить программу?(Y/N)")
            if soglasie(admission.lower()) == True:
                break
        if c == "<":
            a = int(input("Введите первое число: "))
            b = int(input("Введите второе число: "))
            MyModule.min(a, b)
            admission = input("Хотите ли вы завершить программу?(Y/N)")
            if soglasie(admission.lower()) == True:
                break
        if c == ">":
            a = int(input("Введите первое число: "))
            b = int(input("Введите второе число: "))
            MyModule.max(a, b)
            admission = input("Хотите ли вы завершить программу?(Y/N)")
            if soglasie(admission.lower()) == True:
                break
    if deystviye(c) == False:
        print('Введите действие корректно')


