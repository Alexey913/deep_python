# Напишите функцию, которая открывает на чтение созданные 
# в прошлых задачах файлы с числами и именами.
# Перемножьте пары чисел. В новый файл сохраните 
# имя и произведение:
# если результат умножения отрицательный, сохраните имя записанное строчными буквами и произведение по модулю
# если результат умножения положительный, сохраните имя прописными буквами и произведение округлённое до целого.
# В результирующем файле должно быть столько же строк, сколько в более длинном файле. 
# При достижении конца более короткого файла, 
# возвращайтесь в его начало.

def gen_common_file(name_file_1: str, name_file_2: str):
    with (
        open(name_file_1, 'r', encoding='utf-8') as names,\
        open(name_file_2, 'r', encoding='utf-8') as numbers,\
        open("./files/total_file", 'w', encoding='utf-8') as total
        ):
        len_numbers = sum(1 for _ in numbers)
        len_names = sum(1 for _ in names)
        for i in range(max(len_numbers, len_names)):
            num_line = read_per_line(numbers)
            # num_res = float(num_line[0])*float(num_line[1])
            print(num_line)


def read_per_line(name_file):
    for line in name_file:
        yield str(line)


if __name__ == "__main__":
    gen_common_file("./files/letters.txt", "./files/numbers.txt")
# Используем метод seek

