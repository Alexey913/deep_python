# Функция получает на вход строку из двух чисел через пробел.
# Сформируйте словарь, где ключом будет
# символ из Unicode, а значением —  его порядковый номер из диапазона, границами которого являются введенные числа.
# Границы диапазона учитывать.

def create_dict(string_numbers):
    # limit_1 = int(string_numbers.split()[0])
    # limit_2 = int(string_numbers.split()[1])
    limit_1, limit_2 = map(int, string_numbers.split())
    dict_numbers = {}
    for i in range(min(limit_1, limit_2), max(limit_1, limit_2) + 1):
        dict_numbers[chr(i)] = i
    return dict_numbers


input_data = input('Введите значения: ')
print(create_dict(input_data))