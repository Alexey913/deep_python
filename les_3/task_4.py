# Создайте вручную список с повторяющимися элементами.
# Удалите из него все элементы, которые встречаются дважды.


list_ = [5, 4, 8, 9, 9, 5, 2, 0, 1, 8, 14, 14, 14]

print(list_)
for item in list_:
    if list_.count(item) == 2:
        while list_.count(item) != 0:
            list_.remove(item)
print(list_)