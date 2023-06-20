# Создайте функцию-генератор.
# Функция генерирует N простых чисел,
# начиная с числа 2.
# Для проверки числа на простоту используйте
# правило: «число является простым, если делится
# нацело только на единицу и на себя».

def is_simple(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def gen_simple(n):
    pos = 2
    increase = 1
    while n > 0:
        if is_simple(pos):
            n -= 1
            yield pos
        if pos == 3:
            increase = 2
        pos += increase

print(*gen_simple(100))