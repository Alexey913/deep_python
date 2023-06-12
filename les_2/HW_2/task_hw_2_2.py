# Напишите программу, которая принимает две строки
# вида “a/b” — дробь с числителем и знаменателем.
# Программа должна возвращать сумму
# и *произведение дробей. Для проверки своего
# кода используйте модуль fractions.

import fractions


def sum_fraction(up_number_1, down_number_1, up_number_2, down_number_2):
    sum_fraction_up_num = up_number_1 * down_number_2 + up_number_2 * down_number_1
    sum_fraction_down_num = down_number_1 * down_number_2
    nod = find_nod(sum_fraction_up_num, sum_fraction_down_num)
    sum_fraction_up_num = int(sum_fraction_up_num / nod)
    sum_fraction_down_num = int(sum_fraction_down_num / nod)
    sum_fraction_list = [str(sum_fraction_up_num), str(sum_fraction_down_num)]
    return sum_fraction_list


def multiplicate_fraction(up_number_1, down_number_1, up_number_2, down_number_2):
    mult_fraction_up_num = up_number_1 * up_number_2
    mult_fraction_down_num = down_number_1 * down_number_2
    nod = find_nod(mult_fraction_up_num, mult_fraction_down_num)
    mult_fraction_up_num = int(mult_fraction_up_num / nod)
    mult_fraction_down_num = int(mult_fraction_down_num / nod)
    multiplicate_fraction_list = [str(mult_fraction_up_num), str(mult_fraction_down_num)]
    return multiplicate_fraction_list


def find_nod(val_1, val_2):
    min_val = min(val_1, val_2)
    nod = 1
    for i in range(1, min_val):
        if val_1 % i == 0 and val_2 % i == 0:
            nod = i
    return nod


fraction_1 = input('Введите первую дробь: ')
fraction_2 = input('Введите вторую дробь: ')

fraction_list_1 = fraction_1.split('/')
fraction_list_2 = fraction_2.split('/')

up_number_1 = int(fraction_list_1[0])
down_number_1 = int(fraction_list_1[1])
up_number_2 = int(fraction_list_2[0])
down_number_2 = int(fraction_list_2[1])
sum_fraction_result = '/'.join(sum_fraction(up_number_1, down_number_1, up_number_2, down_number_2))
mult_fraction_result = '/'.join(multiplicate_fraction(up_number_1, down_number_1, up_number_2, down_number_2))

print(f"{fraction_1} + {fraction_2} = {sum_fraction_result}")
print(f"{fraction_1} x {fraction_2} = {mult_fraction_result}")

f_1 = fractions.Fraction(up_number_1, down_number_1)
f_2 = fractions.Fraction(up_number_2, down_number_2)
print(f"\nПроверка: сумма - {f_1 + f_2}\n\
          произведение - {f_1 * f_2}")