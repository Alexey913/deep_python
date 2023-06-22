# Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

from sys import platform


# def return_path_name_extention(abs_path: str) -> tuple:
#     if platform == "win32":
#         symbol = "\\"
#     else:
#         symbol = "/"
#     return (symbol.join(abs_path.split(symbol)[:-1]), *(abs_path.split(symbol)[-1].split(".")))


# print(return_path_name_extention("\\Users\share\Производственное управление\Папки сотрудников\Шевцов А.П\Доп.работы\ \
# Левый берег р.Москва\Рабочие материалы\_08-01-01 Устройство объездных дорог.xlxs"))


def return_path_name_extention(abs_path: str) -> tuple:
    if platform == "win32":
        symbol = "\\"
    else:
        symbol = "/"
    *path, file_name = abs_path.rsplit(symbol, 1)
    return *path, *file_name.split(".")


print(return_path_name_extention(input("Введите путь к файлу: ")))
