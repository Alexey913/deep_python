#  Пользователь вводит строку текста.
#  Подсчитайте сколько раз встречается
# каждая буква в строке без использования
# метода couant и с ним.
#  Результат сохраните в словаре, где ключ —
# символ, а значение — частота встречи
# символа в строке.
#  Обратите внимание на порядок ключей.
# Объясните почему они совпадают
# или не совпадают в ваших решениях.


input_string = input('Введите строку: ')
dict_quantity_symbols = {}
dict_quant_without_count = {}
for val in input_string:
    dict_quantity_symbols[val] = input_string.count(val)
print(dict_quantity_symbols)

for val in input_string:
    count = 0
    for quant in input_string:
        if quant == val:
            count+=1
    dict_quant_without_count [val] = count

print(dict_quant_without_count)