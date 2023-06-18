# Функция принимает на вход три списка одинаковой длины:
# имена str, 
# ставка int, 
# премия str с указанием процентов вида «10.25%».
# Вернуть словарь с именем в качестве ключа и суммой 
# премии в качестве значения. 
# Сумма рассчитывается как ставка умноженная на процент премии.

def get_prize(names, salaries, percents) -> dict:
    prize = {}
    for name, salary, percent in zip(names, salaries, percents):
        prize[name] = salary * float(percent[:-1]) / 100
    return prize

names = ['Иванов', 'Петров', 'Сидоров']
salaries = [10000, 20000, 30000]
percents = ['10.25%', '12.15%', '14.20%']

print(get_prize(names, salaries, percents))