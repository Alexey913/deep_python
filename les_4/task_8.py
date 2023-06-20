# ✔ Создайте несколько переменных заканчивающихся и не оканчивающихся на «s». 
# ✔ Напишите функцию, которая при запуске заменяет содержимое переменных 
# оканчивающихся на s (кроме переменной из одной буквы s) на None. 
# ✔ Значения не удаляются, а помещаются в одноимённые переменные без s на конце

def change_name_var():
    change_names_dict = globals()
    new_dict_names = {}
    for key in change_names_dict:
        is_s_name = key[-1]
        if is_s_name == "s" and key != is_s_name:
            new_dict_names[key[0:-1]] = change_names_dict.get(key)
            change_names_dict[key] = None
    for key, val in new_dict_names.items():
        change_names_dict[key] = val
    

names = ["Вася", "Петя", "Жучка"]
dates = "22.09.2010"
numbers = 80
s = "s"
set_var = {4, 6, 8, 11}
one_more = 8.6

print(globals())
print(f"\nНачальные переменные - {names}, {dates}, {numbers}, {s}, {set_var}, {one_more}\n")
change_name_var()
print(globals())
print(f"\nФинальные переменные - {names}, {dates}, {numbers}, {s}, {set_var}, {one_more}\n")
print(f"Новые переменные - {name}, {date}, {number}, {s}")