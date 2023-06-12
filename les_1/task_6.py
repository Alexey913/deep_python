# Напишите программу, которая запрашивает год и проверяет его на високосность.
# Распишите все возможные проверки в цепочке elif
# Откажитесь от магических чисел
# Обязательно учтите год ввода Григорианского календаря
# В коде должны быть один input и один print


START_GRIGORIAN_CALENDAR = 1582
MULTIPLY_4 = 4
MULTIPLY_100 = 100
MULTIPLY_400 = 400

year = int(input('Введите год в формате yyyy: '))
leap_year = None
if year < START_GRIGORIAN_CALENDAR:
    leap_year = "Год был до принятия Григорианского календаря!"
elif year % MULTIPLY_4 != 0 or \
     year % MULTIPLY_100 == 0 and year % MULTIPLY_400 != 0:
    leap_year = "Год не является високосным!"
else:
    leap_year = "Год является високосным!"
print(leap_year)
