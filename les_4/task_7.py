#  Функция получает на вход словарь с названием компании в качестве ключа
# и списком с доходами и расходами (3-10 чисел) в качестве значения.
#  Вычислите итоговую прибыль или убыток каждой компании. Если все компании
# прибыльные, верните истину, а если хотя бы одна убыточная — ложь.

def count_profit(input_dictionary: dict) -> dict:
    result_dictionary = {}
    for key, val in input_dictionary.items():
        result_dictionary[key] = sum(val)
    return result_dictionary


def is_all_profit(input_dictionary: dict) -> bool:
    if all(map(lambda x: x > 0, input_dictionary.values())):
        return True
    return False


start_dictionary = {"Рога": [10000, -5000, 20000], "Копыта": [-8000, 10000, -5000, 10000, 4000], "Хвосты": [8000, 10000, -50000, 10000, -4000]}
print("Итоговая прибыль компаний:\n", count_profit(start_dictionary))
print("Все компании прибыльные?", is_all_profit(count_profit(start_dictionary)))