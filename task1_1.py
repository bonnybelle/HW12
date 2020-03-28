"""
1. Реализовать иерархию классов геометрических фигур. Базовый класс должен обязывать потомков реализовать методы -
периметр и площадь. Потомки:
Треугольник:
        конструктор: принимает список сторон и проверяет, что в списке сторон ровно 3
        периметр
        площадь
Прямоугольник: все аналогично треугольнику, только 2 стороны
Круг: все аналогично треугольнику, только принимает радиус
"""

import math
import sys


class Figure:
    def P(self):
        raise Exception('Error')

    def S(self):
        raise Exception('Error')


class Triangle(Figure):
    def __init__(self, sides):
        self.sides = sides
        for i in self.sides:
            if i <= 0:
                print('Значение не может быть отрицательным или нулевым.')
                sys.exit()
        if len(self.sides) != 3:
            print('Должны быть введены 3 стороны.')
            sys.exit()

    def P(self):
        p = sum(self.sides)
        return p

    def S(self):
        p1 = sum(self.sides) / 2
        s = (p1 * (p1 - self.sides[0]) * (p1 - self.sides[1]) * (p1 - self.sides[2])) ** (1 / 2)
        return s


class Rectangle(Figure):
    def __init__(self, sides):
        self.sides = sides
        for i in self.sides:
            if i <= 0:
                print('Значение не может быть отрицательным или нулевым.')
                sys.exit()
        if len(self.sides) != 2:
            print('Должны быть введены 2 стороны.')
            sys.exit()

    def P(self):
        p = sum(self.sides) * 2
        return p

    def S(self):
        s = self.sides[0] * self.sides[1]
        return s


class Round(Figure):
    def __init__(self, rad):
        self.radius = rad
        if self.radius <= 0:
            print('Значение не может быть отрицательным или нулевым.')
            sys.exit()

    def P(self):
        p = 2 * math.pi * self.radius
        return p

    def S(self):
        s = math.pi * self.radius ** 2
        return s


t = Triangle([3, 4, 5])
r = Rectangle([3, 4])
kolo = Round(9)

print('Периметр треугольника:', t.P(), '\nПлощадь треугольника:', t.S())
print('\nПериметр прямоугольника:', r.P(), '\nПлощадь прямоугольника:', r.S())
print('\nПериметр круга:', kolo.P(), '\nПлощадь круга:', kolo.S())
