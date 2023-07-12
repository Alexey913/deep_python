# Создайте класс студента.
# Используя дескрипторы проверяйте ФИО на первую заглавную букву
# и наличие только букв. Названия предметов должны загружаться
# из файла CSV при создании экземпляра.
# Другие предметы в экземпляре недопустимы.
# Для каждого предмета можно хранить оценки (от 2 до 5)+
# и результаты тестов (от 0 до 100).+
# Также экземпляр должен сообщать средний балл по тестам +
# для каждого предмета и по оценкам всех предметов вместе взятых. +

import csv
import json
from random import randint as rnd

_DOWN_LIMIT_SUBJECT = 2
_UP_LIMIT_SUBJECT = 5
_DOWN_LIMIT_TEST = 0
_UP_LIMIT_TEST = 100
_SUBJECT = "предмет"
_TEST = "тест"
_LIST_DSCIPLINE = "list.csv"

class Descript:

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def validate(self, value):
        if value > 0:
            self.side = value
        else:
            raise ValueError(
                'Значение длины стороны не должно быть отрицательным')


class Student:
    __FILL_SUBJECTS = False
    def __init__(self, *args, list_disciplines=_LIST_DSCIPLINE):
        self.dict_discipline = self.fill_discipline(list_disciplines)
        if len(args) == 3:
            self._surname, self._name, self._patronymic = args
        elif len(args) == 1:
            self._surname, self._name, self._patronymic = args[0].split()
        else:
            raise ValueError("Необходимо ввести ФИО одной строкой или отдельными значениями")
        
    def fill_discipline(self, list_disciplines):
        temp_dict = {}
        with open(list_disciplines, 'r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            for line in reader:
                temp_dict[line[0]] = line[1]
        return temp_dict
    
    def average_subject(self):
        if self.__FILL_SUBJECTS:
            sum = 0
            count = 0
            for name_sub, kind in self.fill_discipline(_LIST_DSCIPLINE).items():
                if kind == _SUBJECT:
                    sum+=self.dict_discipline[name_sub]
                    count+=1
            return sum/count
        else:
            return None
            
    def average_test(self):
        if self.__FILL_SUBJECTS:
            sum = 0
            count = 0
            for name_sub, kind in self.fill_discipline(_LIST_DSCIPLINE).items():
                if kind == _TEST:
                    sum+=self.dict_discipline[name_sub]
                    count+=1
            return sum/count
        else:
            return None


    def __str__(self):
        if self.__FILL_SUBJECTS:
            return f"{self._surname} {self._name[0]}.{self._patronymic[0]}.\n\t" +\
            "\n\t".join(f"{discipline}: {score}" for discipline, score in self.dict_discipline.items()) +\
            f"\nСредний бал по предметам: {self.average_subject()}\tСредний бал по тестам: {self.average_test()}"
        else:
            return f"{self._surname} {self._name[0]}.{self._patronymic[0]}.\n\t" +\
            "Оценки не выставлены"
            
        


    def generate_scores(self):
        with open(f"{self._surname}_{self._name[0]}_{self._patronymic[0]}.json", "w", encoding='utf-8') as f:
            for name_sub, kind in self.dict_discipline.items():
                if kind == _SUBJECT:
                    self.dict_discipline[name_sub] = rnd(_DOWN_LIMIT_SUBJECT, _UP_LIMIT_SUBJECT)
                elif kind == _TEST:
                    self.dict_discipline[name_sub] = rnd(_DOWN_LIMIT_TEST, _UP_LIMIT_TEST)
            json.dump({f"{self._surname} {self._name[0]}.{self._patronymic[0]}":self.dict_discipline}, f, indent=2, ensure_ascii=False)
        self.__FILL_SUBJECTS = True

    @property
    def name(self):
        return self._name
    
    @property
    def surname(self):
        return self._surname
    
    @property
    def patronymic(self):
        return self._patronymic


        
if __name__ == "__main__":
    p = Student("Петров", "Иван", "Иванович")
    r = Student("Иванов Петр Аркадьевич")
    print(p)
    r.generate_scores()
    print(r)
    print(p.average_subject())
    print(r.average_test())





