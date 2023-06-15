# Напишите программу, которая вычисляет площадь 
# круга и длину окружности по введённому диаметру. 
# Диаметр не превышает 1000 у.е. 
# Точность вычислений должна составлять 
# не менее 42 знаков после запятой.

import math
import decimal

decimal.getcontext().prec = 42
while True:
    diameter = int(input('Введите диаметр окружности от 1 до 1000: '))
    if diameter < 1 or diameter > 1000:
        print("Попробуйте еще раз!")
    else:
        break
length_of_circle = decimal.Decimal(2 * math.pi * diameter / 2)
square = decimal.Decimal(math.pi * (diameter/2) ** 2)

print (f"Длина окружности равна {length_of_circle}")
print (f"Площадь круга равна {square}")