name = input("Введите ваше имя: ")
def describe_person(name, age=30):
    # name.lower().title()
    print(f"Привет,{name.title()}!Я слышал тебе {age} лет.")
describe_person(name)