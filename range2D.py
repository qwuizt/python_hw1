import math


x1 = float (input("Введите x1: "))
y1 = float (input("Введите y1: "))
x2 = float (input("Введите x2: "))
y2 = float (input("Введите y2: "))
range = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

print(round(range, 3))