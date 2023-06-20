from task_5 import riddle
def some_riddles():
    dict_riddle = {"Зимой и летом одним цветом":["Ёлка", "елка", "ёлка", "Елка", "ель", "Ель"],\
                   "Не расческа, а свистит":["Свисток", "Свист", "свисток"],
                   "Не ведро, а гавкает":["Собака", "пес", "Щенок"]}
    for rid, answ in dict_riddle.items():
        riddle(rid, answ)
