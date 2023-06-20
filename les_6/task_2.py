
# Создайте модуль с функцией внутри. 
# Функция принимает на вход три целых числа: нижнюю и верхнюю границу и количество попыток. 
# Внутри генерируется случайное число в указанных границах и пользователь должен угадать его за заданное число попыток. 
# Функция выводит подсказки “больше” и “меньше”. 
# Если число угадано, возвращается истина, а если попытки исчерпаны - ложь.


from random import randint

def find_number (lower_limit, upper_limit, try_quantity):
    print(f"Я загадаю случайное число в диапазоне от 0 до 1000.\nПопробуй его отгадать за {try_quantity} попыток")
    num = randint(lower_limit, upper_limit)
    try_counter = try_quantity
    while try_counter > 0:
        input_data = int(input(f"Осталось {try_counter} попыток. Введите число: "))
        if input_data < lower_limit or input_data > upper_limit:
            print("Неверный ввод!")
        elif num == input_data:
            return True
        elif num > input_data:
            print(f"Больше!")
        else:
            print(f"Меньше!")
        try_counter -= 1
    else:
        print(f"Все попытки исчерпаны. Я загадал число {num}")
    return False
