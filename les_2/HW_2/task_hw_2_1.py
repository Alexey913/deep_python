# Напишите программу, которая получает целое
# число и возвращает его шестнадцатеричное
# строковое представление. Функцию hex
# используйте для проверки своего результата.

BASE = 16


def convert(input_number: int) -> str:
    output_number = []
    translate_to_hex = '0123456789abcdef'
    while input_number:
        output_number.insert(0, translate_to_hex[input_number % BASE])
        input_number //= BASE
    return ''.join(output_number)


input_number = int(input('Введите число: '))

print(f"dec - {input_number}, hex - {convert(input_number)}")
print(hex(input_number) + " (проверка)")