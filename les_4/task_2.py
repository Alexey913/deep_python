# Напишите функцию, которая принимает строку текста. 
# Сформируйте список с уникальными кодами Unicode каждого 
# символа введённой строки отсортированный по убыванию.

def sort_string (input_string):
    # new_list = list(input_string)
    list_unicode = []
    for item in set(input_string):
        list_unicode.append(ord(item))
    list_unicode.sort(reverse=True)

    return list_unicode



print(sort_string("Привет меня зовут Алексей"))
