# Функция получает на вход список чисел и два индекса.
# Вернуть сумму чисел между между переданными индексами.
# Если индекс выходит за пределы списка, сумма считается
# до конца и/или начала списка.

def sum_between_elements(list_numbers: list, index_1: int, index_2: int) -> int:
    if index_1 > index_2:
        index_1, index_2 = index_2, index_1
    if index_1 < 0:
        limit_down = 0
    else:
        limit_down = index_1
    if index_2 >= len(list_numbers):
        limit_up = len(list_numbers) - 1
    else:
        limit_up = index_2
    sum = 0
    for i in range(limit_down, limit_up+1):
        sum += list_numbers[i]
    return sum


input_list = list(map(int, input(
    'Введите числа списка через пробел: ').split()))
limit_1, limit_2 = map(int, input(
    'Введите индексы элементов через пробел: ').split())

print(f"Сумма равна: {sum_between_elements(input_list, limit_1, limit_2)}")
