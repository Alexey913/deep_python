# Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.

def print_table(start_pos, stop_pos, count_pos, transfer_pos):
    count_reset = count_pos
    indent = None
    for i in range(start_pos, stop_pos):
        while (count_pos < transfer_pos):
            if (i == 10):
                indent = " "
            elif i * count_pos // 10 == 0:
                indent = "   "
            else:
                indent = "  "
            print(count_pos, " x ", i, " =", indent, count_pos * i, end="        ")
            count_pos += 1
        print("")
        count_pos = count_reset


START = 2
STOP = 11
COUNT = 2
TRANSFER = 6
print("")
print_table(START, STOP, COUNT, TRANSFER)
print("")
print_table(START, STOP, TRANSFER, STOP-1)
print("")
