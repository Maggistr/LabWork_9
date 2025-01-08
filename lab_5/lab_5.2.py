import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius

    def set_radius(self, new_radius):
        self.radius = new_radius

    def get_circle_length(self):
        return 2 * math.pi * self.get_radius()

    def get_circle_square(self):
        return math.pi * self.get_radius() * self.get_radius()


x = int(input('Введите радиус: '))
if x > 0:
    circle = Circle(x)
    print(f'Ваш радиус: {circle.get_radius()}')
else:
    print('Радиус не может быть отрицательным.')

y = int(input('Введите новый радиус: '))
if y > 0:
    circle = Circle(y)
    print(f'Ваш радиус: {circle.get_radius()}')
else:
    print('Радиус не может быть отрицательным.')

length = Circle(y)
print(f'Длина окружности с радиусом {circle.get_radius()} равен {circle.get_circle_length()}')

square = Circle(y)
print(f'Длина окружности с радиусом {circle.get_radius()} равен {circle.get_circle_square()}')

