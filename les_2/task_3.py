# * Напишите программу, которая получает целое число и возвращает 
# его двоичное, восьмеричное строковое представление.
# * Функции bin и oct используйте для проверки своего 
# результата, а не для решения.
# Дополнительно:
# * Попробуйте избежать дублирования кода 
# в преобразованиях к разным системам счисления
# * Избегайте магических чисел
# * Добавьте аннотацию типов где это возможно

def convert (input_number: int, base: int) -> str:
    output_number = list ()
    while input_number > 0:
        output_number.append(str(input_number % 2))
        input_number //= base
    output_number.reverse()
    return ''.join(output_number)

input_number = int(input('Введите число: '))
base = int(input('Введите основание: '))
print(convert(input_number, base))
print (bin(input_number) + " - в двоичной системе счисления")
print (oct(input_number) + " - в восьмеричной системе счисления")


# def convert(b, c):
#     if b == 0:
#         return l
#     dig = b % c
#     l.append(dig)
#     convert(b // c, c)

# l = []

# a = int(input('введите число: '))
# d = int(input('введите систему счисления: '))
# convert(a, d)
# l.reverse()
# print('форма числа по основанию', d)
# for i in l:
#     print(i, end='')
# print('\n')
# if d == 2:
#     print(bin(a))
# elif d == 8:
#     print(oct(a))