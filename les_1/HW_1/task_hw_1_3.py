# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
# Программа должна подсказывать «больше» или «меньше» после каждой попытки.
# Для генерации случайного числа используйте код:
# from random import randint
# num = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint

LOWER_LIMIT = 1
UPPER_LIMIT = 1000


def check(secret_number, input_number):
    if secret_number == input_number:
        return True
    else:
        return False


def comparison(secret_number, input_number):
    if secret_number > input_number:
        return "Больше!"

    return "Меньше!"


print("Я загадаю случайное число в диапазоне от 0 до 1000.\nПопробуй его отгадать за 10 попыток")
num = randint(LOWER_LIMIT, UPPER_LIMIT)
try_counter = 10
while try_counter > 0:
    input_data = int(input(f"Осталось {try_counter} попыток. Введите число: "))
    if input_data < LOWER_LIMIT or input_data > UPPER_LIMIT:
        print("Неверный ввод!")
    elif check(num, input_data):
        print(f"Верно! Я загадал число {input_data}")
        break
    else:
        print(comparison(num, input_data))
        try_counter -= 1
else:
    print(f"Все попытки исчерпаны. Я загадал число {num}")
