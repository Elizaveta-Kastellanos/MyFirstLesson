import math
# Homework

# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, 
# и проверяет, является ли этот день выходным.
# SATURDAY_NUMBER_CONST = 6
# SUNDAY_NUMBER_CONST = 7
# num = None
# while True:
#     num = int(input('Введите цифру обозначающую день недели: '))
#     if (num > 0) and (num < 8):
#         break
# if (num == SATURDAY_NUMBER_CONST) or (num == SUNDAY_NUMBER_CONST):
#     print('да')
# else:
#     print('нет')

# 3. Напишите программу, которая принимает на вход координаты точки (X и Y), 
#    причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
#    в которой находится эта точка (или на какой оси она находится).


# while True:
#     x = float(input('Введите X: '))
#     y = float(input('Введите Y: '))
#     if (x != 0) and (y != 0):
#         break   

# if (x > 0) and (y > 0):
#     print('Первая четверть')
# elif (x < 0) and (y > 0):
#     print('Вторая четверть')
# elif (x < 0) and (y < 0):
#     print('Третья четверть')
# elif (x > 0) and (y < 0):
#     print('Четвертая четверть')
# else:
#     ('Четверть не найдена')

# 4. Напишите программу, которая по заданному номеру четверти, 
#    показывает диапазон возможных координат точек в этой четверти (x и y).

while True:
    quarter = int(input('Введите номер четверти: '))
    if (quarter >= 1) and (quarter <=4):
        break
if quarter == 1:
    print('Диапазон первой четверти у X и Y: от 1 до 500')
elif quarter == 2:
    print('Диапазон второй четверти: X = -500 до -1; Y = 1 до 500')
elif quarter == 3:
    print('Диапазон третей четверти: X = -500 до -1; Y = -500 до -1')
elif quarter == 4:
    print('Диапазон четвертой четверти: X = 1 до 500; Y = -500 до -1')
else:
    print('Четверть не найдена')

# 5. Напишите программу, которая принимает на вход координаты двух точек и 
#    находит расстояние между ними в 2D пространстве. Пример: - A (3,6); B (2,1) -> 5,09

a = input('Введите координаты точки A: X1 и Y1 через пробел: ').split()
b = input('Введите координаты точки B: X2 и Y2 через пробел: ').split()
a_list = [float(i) for i in a]
b_list = [float(i) for i in b]
distance_between_points = math.sqrt((b_list[0] - a_list[0])**2 + (b_list[1] - a_list[1])**2)
print('{:.3f}'.format(distance_between_points))

# 2. Напишите программу для. проверки истинности утверждения 
#    ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
x = int(input('Введите Х: '))
y = int(input('Введите Y: '))
z = int(input('Введите Z: '))
left_part = not (x or y or z)
right_part = not x and not y and not z
if left_part == right_part:
    print('Выражение истинное')
else:
    print('Выражение ложное')



















        


    



     