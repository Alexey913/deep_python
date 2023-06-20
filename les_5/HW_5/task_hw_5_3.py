# Создайте функцию генератор чисел Фибоначчи

QUANTITY_NUM = 20

def fibo_gen(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


for i, num in enumerate(fibo_gen(QUANTITY_NUM), start=1):
    print(f'Число {i} - {num}')
