x = 0
while x ==0:
    try:
        num = int(input("Введите число:"))
        break
    except ValueError:
        print("Введите лучше число.")
num += 1
for i in range (1 , num):
    print(i)
