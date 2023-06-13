# Создайте вручную кортеж содержащий элементы разных типов.
# Получите из него словарь списков, где:
# ключ — тип элемента,
# значение — список элементов данного типа.

new_tuple = (1, "Hello", "world", 214, 32.4, [1,4,6], (12, 56, 87, 88), ("Geek", "Brains"))
dict_type = {}
for items in new_tuple:
    values = [item for item in new_tuple if type(item) is type(items)] 
    dict_type[type(items)] = values
    # или dict_type.setdefault(type(item), []).append(item)
    # или dict_type[type(item)] = dict_type.get(type(item), []) + [item]
print(dict_type)