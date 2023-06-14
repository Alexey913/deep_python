# Создайте в переменной data список значений разных типов перечислив их через запятую внутри квадратных скобок. 
# Для каждого элемента в цикле выведите:
# * порядковый номер начиная с единицы
# * значение
# * адрес в памяти
# * размер в памяти
# * хэш объекта
# * результат проверки на целое число только если он положительный
# * результат проверки на строку только если он положительный
# Добавьте в список повторяющиеся элементы и сравните на результаты.

data = [23, "GeekBrains", 3.141592, True, 23, "GeekBrains", None]
for i, val in enumerate (data):
    print(f"Порядковый номер: {i + 1}\n\
           Значение: {val}\n\
           Адрес в памяти: {id(val)}\n\
           Размер в памяти: {val.__sizeof__()}\n\
           Хэш: {hash(val)}")
    if (type(val) == int):
        print (f"\t   Это целое число {val}")
    elif (isinstance(val,str)):
        print (f"\t   Это строка - {val}")