# Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
# Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
# Для простоты договоримся, что год может быть в диапазоне [1, 9999]. 
# Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь. 
# Проверку года на високосность вынести в отдельную защищённую функцию.

# _MULTIPLY_4 = 4
# _MULTIPLY_100 = 100
# _MULTIPLY_400 = 400



# def true_year (date):
#     date_list = date.split(".")
#     if len(date_list) > 3:
#         return False
#     # day, month, year = 
#     if not int(date_list[2]) in range(1, 10000):
#         return False
#     for month, day in dict_month.items():
#         if month == date_list[1] and int(date_list[0]) in range(day+1):
#             return True
#         if date_list[1] == "02" and _is_leap_year(int(date_list[2]))\
#             and int(date_list[0]) in range(30):
#             return True
#     return False



# def _is_leap_year (year_val):
#     if year_val % _MULTIPLY_4 != 0 or \
#         year_val % _MULTIPLY_100 == 0 and year_val % _MULTIPLY_400 != 0:
#         return False
#     return True

# dict_month = {"01":31,"02":28,"03":31,"04":30,"05":31,"06":30,"07":31,"08":31,"09":30,"10":31,"11":30,"12":31}

# print(true_year("28.02.0201"))


_MULTIPLY_4 = 4
_MULTIPLY_100 = 100
_MULTIPLY_400 = 400


def _is_leap_year (year_val):
    if year_val % _MULTIPLY_4 != 0 or \
        year_val % _MULTIPLY_100 == 0 and year_val % _MULTIPLY_400 != 0:
        return False
    return True
    
    
def check_date(date):
    date_list = date.split(".")
    if len(date_list) != 3:
        return False
    day, mounth, year = list(map(int, date_list))
    if (len(date_list[0]) != 2 or len(date_list[1]) != 2 or len(date_list[2]) != 4):
        return False
    if not year in range(1,10000) or not mounth in range(1,13) or not day in range(1,31):
        return False
    if day == 31 and mounth in [2, 4, 6, 9, 11]:
        return False
    if mounth == 2 and (day == 30 or day == 29 and _is_leap_year(year) is False):
        return False
    return True
    
    
date = input('Введите дату для проверки: ')
print(check_date(date))
