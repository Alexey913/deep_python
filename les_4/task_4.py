#  Функция получает на вход список чисел. 
#  Отсортируйте его элементы in place без использования 
# встроенных в язык сортировок. 
#  Как вариант напишите сортировку пузырьком. 
# Её описание есть в википедии.

def sort_ (list_numbers):
    # for i, item_i in enumerate(list_numbers):
    #     for j in range(i, len(list_numbers)):
    #         if item_i > list_numbers[j]:
    for i in range (len(list_numbers)):
        for j in range(i, len(list_numbers)):
            if list_numbers[i] > list_numbers[j]:
                list_numbers[i], list_numbers[j] = list_numbers[j], list_numbers[i]

list_num = [5, 9, 1, -8, 0]
print(list_num)
sort_(list_num)            
print(list_num)