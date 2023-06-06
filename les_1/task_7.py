# Пользователь вводит число от 1 до 999. Используя операции с числами
# сообщите что введено: цифра, двузначное число или трёхзначное число.
# Для цифры верните её квадрат, например 5 - 25
# Для двузначного числа произведение цифр, например 30 - 0
# Для трёхзначного числа его зеркальное отображение, например 520 - 25
# Если число не из диапазона, запросите новое число
# Откажитесь от магических чисел
# В коде должны быть один input и один print

MIN_LIMIT = 1
MAX_LIMIT = 999

while True:
    input_number = int(input(f"Введите число от {MIN_LIMIT} до {MAX_LIMIT}: "))
    if input_number < MIN_LIMIT or input_number > MAX_LIMIT:
        input_number = -1
    else:
        break
if input_number // 100 > 0:
    message = "Введено трехзначное число. Зеркальное отображение числа равно"
    result = input_number % 10 * 100 + (input_number // 10) % 10 * 10 + input_number // 100
elif input_number // 10 > 0:
    message = "Введено двухзначное число. Произведение цифр числа равно"
    result = (input_number // 10) * (input_number % 10)
else:
    message = "Введена цифра. Квадрат числа равен"
    result = input_number ** 2
print(message, result)