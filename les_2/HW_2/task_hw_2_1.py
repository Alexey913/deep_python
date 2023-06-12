# Напишите программу, которая получает целое
# число и возвращает его шестнадцатеричное
# строковое представление. Функцию hex
# используйте для проверки своего результата.

BASE = 16


def convert(input_number: int) -> str:
    output_number = []
    translate_to_hex = {10:'a', 11:'b', 12:'c', 13:'d', 14:'e', 15:'f'}
    while input_number > 0:
        delimeter = input_number % BASE
        for keys_for_hex in translate_to_hex:
            if delimeter == keys_for_hex:
                delimeter = translate_to_hex.get(keys_for_hex)
        output_number.insert(0, str(delimeter))
        input_number //= BASE
    return ''.join(output_number)


input_number = int(input('Введите число: '))

print(f"dec - {input_number}, hex - {convert(input_number)}")
print(hex(input_number) + " (проверка)")