# Функция получает на вход список чисел.
# Отсортируйте список по убыванию суммы цифр


def sum_digit(number):
    return sum(map(int, str(number)))


def sort_dict(list_num):
    return dict(sorted((zip(map(sum_digit, list_num), list_num)), key=lambda x: x[0], reverse=True))


list_num = [51, 49, 11, 18, 20]
print(list_num)
print(sort_dict(list_num))
