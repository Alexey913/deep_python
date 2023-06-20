# Улучшаем задачу 2. 
# Добавьте возможность запуска функции “угадайки” из модуля в командной строке терминала. 
# Строка должна принимать от 1 до 3 аргументов: параметры вызова функции. 
# Для преобразования строковых аргументов командной строки в числовые параметры используйте генераторное выражение.



from random import randint
from sys import argv

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

if __name__ == "__main__":
    _, *params = argv
    print(find_number(*map(int, params)))




# from random import randint
# from sys import argv

# LOWER_LIMIT = 0
# UPPER_LIMIT = 10
# NUM_OF_ATTEMPTS = 3

# def game(low=0, high=10, num_of_attempts=3):
#     number = randint(low, high)
#     attempt = 0
#     print(
#         f'Программа загадывает число от {low} до {high}. Необходимо угадать число за {attempt} попыток.')
#     while attempt < num_of_attempts:
#         attempt += 1
#         user_number = int(input(f'Попытка номер {attempt}. Введите число: '))
#         if user_number < number:
#             print('Меньше')
#         elif user_number > number:
#             print('Больше')
#         else:
#             print(f'Вы отгадали с {attempt} попытки!')
#             return True
#     else:
#         print(f'Вы использовали все {attempt} попыток и не отгадали число. Было загадано число {number}. Вы проиграли.')
#         return False

# if __name__ == '__main__':
#     print(argv)
#     _, *params = argv
#     print(game(*map(int, params)))

# # python sem_06_03.py 0 10 3