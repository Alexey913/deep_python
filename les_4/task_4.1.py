# Функция получает на вход список чисел. 
# Отсортируйте список по убыванию суммы цифр

def sum_digit (number):
    return sum(map(int, str(number)))

def sort_ (list_numbers: list):
   return sorted(list_numbers, key = sum_digit, reverse=True)

list_num = [51, 49, 11, 18, 20]
print(list_num)
print(sort_(list_num))            