import math
l = input('Введите фигуру на английском: ')
def rectangle(a, b):
    global k
    k = a * b
def triangle(a, b, c):
    global s
    p = (a + b + c) / 2
    from math import sqrt
    s = sqrt(p * (p - a) * (p - b) * (p - c))
def circle(r):
    global g
    pi = 3.14
    g = pi * r ** 2
if l == 'rectangle':
    print("Длины сторон прямоугольника:")
    a = float(input("a = "))
    b = float(input("b = "))
    rectangle(a, b)
    print('Площадь прямоугольника равна: ', k)
elif l == 'triangle':
    print("Длины сторон треугольника:")
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))
    triangle(a, b, c)
    print('Площадь треугольника равна: ', s)
elif l == 'circle':
    r = float(input("Радиус круга R = "))
    circle(r)
    print('Площадь круга равна: ', g)
else:
    print('Введено не верно')
