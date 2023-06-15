# Три друга взяли вещи в поход. Сформируйте
# словарь, где ключ — имя друга, а значение —
# кортеж вещей. Ответьте на вопросы:
# Какие вещи взяли все три друга
# Какие вещи уникальны, есть только у одного друга
# Какие вещи есть у всех друзей кроме одного
# и имя того, у кого данная вещь отсутствует
# Для решения используйте операции
# с множествами. Код должен расширяться
# на любое большее количество друзей.

from random import randint
list_of_items = ["Котелок", "Палатка", "Гитара", "Мангал",
                 "Шампура", "Тушенка", "Мясо", "Вода", "Сухпаек", "Спички"]
list_of_people = ["Вася", "Петя", "Валера"]
dict_list_for_hike = {}
temp_quantity_items = set()
quantity_items = int(len(list_of_items) / len(list_of_people)) * 2

for human in list_of_people:
    for _ in range(quantity_items):
        temp_quantity_items.add(
            list_of_items[randint(0, len(list_of_items)-1)])
    dict_list_for_hike[human] = tuple(temp_quantity_items)
    temp_quantity_items = set()

print("Друзья взяли следующие вещи:")
print(dict_list_for_hike)

common_items = set()

print("Все вместе они взяли:")
for human in list_of_people:
    common_items = common_items.union(set(dict_list_for_hike.get(human)))
print(common_items)

items_except = common_items

print("Каждый из друзей взял:")
for human in list_of_people:
    common_items = common_items.intersection(set(dict_list_for_hike.get(human)))
print(common_items)

print("Уникальные вещи:")
unique_items = set()
sum_items = set()
for human in list_of_people:
    for key, val in dict_list_for_hike.items():
        if human != key:
            sum_items = sum_items.union(val)
            unique_items = unique_items.union(val)
        else:
            unique_items = unique_items.union(val)
    print(f"\t- взял только {human} - {unique_items.difference(sum_items)}")
    unique_items = set()
    sum_items = set()
    
print("Кто-то что-то не взял:")
sum_items = set()
for human in list_of_people:
    for key, val in dict_list_for_hike.items():
        sum_items = sum_items.union(val)
    print(f"\t- {human} не взял - {sum_items.difference(set(dict_list_for_hike[human]))}")
    sum_items = set()
