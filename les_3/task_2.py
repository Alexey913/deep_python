# Пользователь вводит данные. Сделайте проверку данных
# и преобразуйте если возможно в один из вариантов ниже:
# Целое положительное число
# Вещественное положительное или отрицательное число
# Строку в нижнем регистре, если в строке есть
# хотя бы одна заглавная буква
# Строку в верхнем регистре в остальных случаях

sign = "Positive"
input_string = input('Введите строку: ')
result = None
if input_string.isnumeric():
    result = int(input_string)
elif input_string.replace(".", '', 1).isnumeric() or input_string.replace(",", '', 1).isnumeric():
    result = float(input_string.replace(',', '.'))
elif input_string.startswith("-") and input_string.replace('-', '', 1).replace('.', '', 1).replace(",", '', 1).isnumeric():
    result = -float(input_string.replace(',', '.').replace('-', ''))
    sign = "Negative"
else:
    for char in input_string:
        if char.isalpha() and char == char.upper():
            result = input_string.lower()
            sign = "Lower string"
            break
        else:
            result = input_string.upper()
            sign = "Upper string"

print (result, type(result), sign)