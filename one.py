import math
from turtle import right
# Homework

# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, 
# и проверяет, является ли этот день выходным.
 
num = int(input('Введите цифру обозначающую день недели: '))
if (num == 6) or (num == 7):
    print('да')
else:
    print('нет')

# 3. Напишите программу, которая принимает на вход координаты точки (X и Y), 
#    причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
#    в которой находится эта точка (или на какой оси она находится).

x = None
while True:
    x = float(input('Введите X: '))
    if (x != 0):
        break   
y = None
while True:
    y = float(input('Введите Y: '))
    if (y != 0):
        break
if (x > 0) and (y > 0):
    print('Первая четверть')
if (x < 0) and (y > 0):
    print('Вторая четверть')
if (x < 0) and (y < 0):
    print('Третья четверть')
if (x > 0) and (y < 0):
    print('Четвертая четверть')

# 4. Напишите программу, которая по заданному номеру четверти, 
#    показывает диапазон возможных координат точек в этой четверти (x и y).

quarter = None
while True:
    quarter = int(input('Введите номер четверти: '))
    if(quarter >= 1) and (quarter <=4):
        break
if (quarter == 1):
    print('Диапазон первой четверти у X и Y: от 1 до 500')
if (quarter == 2):
    print('Диапазон второй четверти: X = -500 до -1; Y = 1 до 500')
if (quarter == 3):
    print('Диапазон третей четверти: X = -500 до -1; Y = -500 до -1')
if (quarter == 4):
    print('Диапазон четвертой четверти: X = 1 до 500; Y = -500 до -1')

# 5. Напишите программу, которая принимает на вход координаты двух точек и 
#    находит расстояние между ними в 2D пространстве. Пример: - A (3,6); B (2,1) -> 5,09

a = input('Введите координаты точки A: X1 и Y1 через пробел: ').split()
b = input('Введите координаты точки B: X2 и Y2 через пробел: ').split()
aList = [float(i) for i in a]
bList = [float(i) for i in b]
distanceBetweenPoins = math.sqrt((bList[0]-aList[0])**2 + (bList[1]-aList[1])**2)
print('{:.3f}'.format(distanceBetweenPoins))

# 2. Напишите программу для. проверки истинности утверждения 
#    ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
x = int(input('Введите Х: '))
y = int(input('Введите Y: '))
z = int(input('Введите Z: '))
leftPart = not (x or y or z)
rightPart = not x and not y and not z
if (leftPart == rightPart):
    print('Выражение истинное')
else:
    print('Выражение ложное')



















        


    



     