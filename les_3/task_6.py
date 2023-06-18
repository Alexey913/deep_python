# Пользователь вводит строку текста. Вывести каждое слово с новой строки.
# Строки нумеруются начиная с единицы.
# Слова выводятся отсортированными согласно кодировки Unicode.
# Текст выравнивается по правому краю так, чтобы у самого длинного
# слова был один пробел между ним и номером строки.

input_string = input("Введите строку: ")
list_string = sorted(input_string.split())
max_len = 1
for i, val in enumerate(list_string):
    if len(val) + len(str(i)) > max_len:
        max_len = len(val) + len(str(i))
for i, val in enumerate(list_string):
    print(f'{i+1}{val:>{max_len}}')