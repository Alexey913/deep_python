# Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: «Число является простым, если делится нацело только на единицу
# и на себя». Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч


print("Введите целое число в диапазоне от 0 до 100 000")
check = False
while True:
    input_data = int(input("Введите число: "))
    if input_data < 0 or input_data > 100000:
        print ("Неверный ввод!")
    else:
        break
if input_data <= 1:
       print(f"Число {input_data} не является ни простым, ни составным!")
else:
    final_pos = int(input_data ** 0.5) + 1
    for i in range (2, final_pos):
        if input_data % i == 0:
            check = True
            break
    if check:
        print(f"Число {input_data} является составным!")
    else:
        print(f"Число {input_data} является простым!")
