# Вручную создайте список с целыми числами, которые
# повторяются. Получите новый список, который содержит
# уникальные (без повтора) элементы исходного списка.
# Подготовьте два решения, короткое и длинное, которое
# не использует другие коллекции помимо списков.
 
from random import randint
 
COUNT=15
 
list_1 = []
for i in range (COUNT):
    list_1.append(randint(COUNT-i, COUNT))
print(list_1)
 
# Перечень уникальных значений
list_2 = []
for i in range(len(list_1)):
    if list_1.count(list_1[i]) == 1:
        list_2.append(list_1[i])
print(list_2)
 
list_3 = []
for item in list_1:
    if item not in list_3:
        list_3.append(item)
print(list_3)
 
list_4 = set(list_1)
print(list_4, type(list_4))
 
list_5 = [*set(list_1)]
print(list_5, type(list_5))