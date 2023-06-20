# Напишите функцию принимающую на вход только ключевые
# параметры и возвращающую словарь, где ключ — значение
# переданного аргумента, а значение — имя аргумента. Если
# ключ не хешируем, используйте его строковое представление

def create_dict_kwargs(**kwargs):
    return_dict = {}
    for key, value in kwargs.items():
        if value.__hash__ is None:
            return_dict[str(value)] = key
        else:
            return_dict[value] = key
    return return_dict


dict_arg = dict(four=4, three=3)
num_arg = 22
str_arg = "Hello"
list_arg = [1, 2, 3]
float_arg = 1.6

print(create_dict_kwargs(arg_1=dict_arg, arg_2=num_arg, arg_3=str_arg, arg_4=list_arg, arg_5=float_arg))
