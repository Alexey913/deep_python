# Нарисовать в консоли ёлку спросив
# у пользователя количество рядов.
# Пример результата:
# Сколько рядов у ёлки? 5
#     *
#    ***
#   *****
#  *******
# *********

quantity_rows = int(input("Сколько рядов у ёлки? "))
count = 1
while quantity_rows > 0:
    spaces = " " * (int(quantity_rows - 1))
    stars = "*" * (count * 2 - 1)
    print(spaces, stars)
    quantity_rows -= 1
    count += 1