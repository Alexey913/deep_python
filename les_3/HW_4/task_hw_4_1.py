# Дан список повторяющихся элементов. Вернуть список 
# с дублирующимися элементами. В результирующем списке 
# не должно быть дубликатов.

start_list = [5, 8, 9, 14, 5, 0, -8, 14, 5, 1, 12, -8]
end_list = []
for val in start_list:
    if start_list.count(val) > 1 and not val in end_list:
        end_list.append(val)

print(start_list)
print(end_list)