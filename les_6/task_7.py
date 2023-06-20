# Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
# Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
# Для простоты договоримся, что год может быть в диапазоне [1, 9999]. 
# Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь. 
# Проверку года на високосность вынести в отдельную защищённую функцию.

_MULTIPLY_4 = 4
_MULTIPLY_100 = 100
_MULTIPLY_400 = 400



def true_year (date):
    date_list = date.split(".")
    if len(date_list) > 3:
        return False
    # day, month, year = 
    if not int(date_list[2]) in range(1, 10000):
        return False
    for month, day in dict_month.items():
        if month == date_list[1] and int(date_list[0]) in range(day+1):
            return True
        if date_list[1] == "02" and _is_leap_year(int(date_list[2]))\
            and int(date_list[0]) in range(30):
            return True
    return False



def _is_leap_year (year_val):
    if year_val % _MULTIPLY_4 != 0 or \
        year_val % _MULTIPLY_100 == 0 and year_val % _MULTIPLY_400 != 0:
        return False
    return True

dict_month = {"01":31,"02":28,"03":31,"04":30,"05":31,"06":30,"07":31,"08":31,"09":30,"10":31,"11":30,"12":31}

print(true_year("28.02.0201"))