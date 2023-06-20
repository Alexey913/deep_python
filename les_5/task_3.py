# Продолжаем развивать задачу 2. 
# Возьмите словарь, который вы получили. 
# Сохраните его итераторатор. 
# Далее выведите первые 5 пар ключ-значение, 
# обращаясь к итератору, а не к словарю.

input_string = set(input("Введите строку: "))
dictionary = {i: ord(i) for i in input_string}
print(dictionary)
iter_dict = iter(dictionary.items())
for _ in range(5):
    print(next(iter_dict))