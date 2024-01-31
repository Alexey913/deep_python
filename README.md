# Курс Погружение в Python
## [Курс Знакомство с Python](https://github.com/Alexey913/python.git)

## [Семинар 1 - Основы Python](les_1/)
### Задания 1 - 5: виртуальное окружение и работа в терминале
### [Задание 6](les_1/task_6.py)
Напишите программу, которая запрашивает год и проверяет его на високосность. Распишите все возможные проверки в цепочке elif. Откажитесь от магических чисел. Обязательно учтите год ввода Григорианского календаря. В коде должны быть один input и один print.
### [Задание 7](les_1/task_7.py)
Пользователь вводит число от 1 до 999. Используя операции с числами сообщите что введено: цифра, двузначное число или трёхзначное число. Для цифры верните её квадрат, например 5 - 25. Для двузначного числа произведение цифр, например 30 - 0. Для трёхзначного числа его зеркальное отображение, например 520 - 25. Если число не из диапазона, запросите новое число. Откажитесь от магических чисел. В коде должны быть один input и один print
### [Задание 8](les_1/task_8.py)
Нарисовать в консоли ёлку, спросив у пользователя количество рядов.
### [Задание 9](les_1/task_9.py)
Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.

## [Домашнее задание 1](les_1/HW_1)
### [Задание 1](les_1/HW_1/task_hw_1_1.py)
Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей. Дано a, b, c - стороны предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны с суммой двух других. Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника с такими сторонами не существует. Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.
### [Задание 2](les_1/HW_1/task_hw_1_2.py)
Напишите код, который запрашивает число и сообщает, является ли оно простым или составным. Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”. Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.
### [Задание 3](les_1/HW_1/task_hw_1_3.py)
- Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа должна подсказывать “больше” или “меньше” после каждой попытки.

## [Семинар 2 - Простые типы данных](les_2/)
### [Задание 2](les_2/task_2.py)
Создайте в переменной data список значений разных типов перечислив их через запятую внутри квадратных скобок. Для каждого элемента в цикле выведите:
* порядковый номер начиная с единицы
* значение
* адрес в памяти
* размер в памяти
* хэш объекта
* результат проверки на целое число только если он положительный
* результат проверки на строку только если он положительный
Добавьте в список повторяющиеся элементы и сравните на результаты.
### [Задание 3](les_2/task_3.py)
Напишите программу, которая получает целое число и возвращает  его двоичное, восьмеричное строковое представление.
Функции bin и oct используйте для проверки своего результата, а не для решения. Дополнительно:
* Попробуйте избежать дублирования кода в преобразованиях к разным системам счисления
* Избегайте магических чисел
* Добавьте аннотацию типов где это возможно
### [Задание 4](les_2/task_4.py)
Напишите программу, которая вычисляет площадь круга и длину окружности по введённому диаметру. Диаметр не превышает 1000 у.е. Точность вычислений должна составлять не менее 42 знаков после запятой.
### [Задание 5](les_2/task_5.py)
Напишите программу, которая решает квадратные уравнения, даже если дискриминант отрицательный. Используйте комплексные числа для извлечения квадратного корня
### [Задание 6](les_2/task_6.py)
Напишите программу банкомат. Начальная сумма равна нулю. Допустимые действия: пополнить, снять, выйти. Сумма пополнения и снятия кратны 50 у.е. Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
После каждой третей операции пополнения или снятия начисляются проценты - 3%. Нельзя снять больше, чем на счёте. При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной. Любое действие выводит сумму денег.

## [Домашнее задание 2](les_2/HW_2)
### [Задание 1](les_2/HW_2/task_hw_2_1.py)
Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление. Функцию hex используйте для проверки своего результата.
### [Задание 2](les_2/HW_2/task_hw_2_2.py)
Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.

## [Семинар 3 - Коллекции](les_3/)
### [Задание 1](les_3/task_3_1.py)
Вручную создайте список с целыми числами, которые повторяются. Получите новый список, который содержит уникальные (без повтора) элементы исходного списка. Подготовьте два решения, короткое и длинное, которое не использует другие коллекции помимо списков.
### [Задание 2](les_3/task_3_2.py)
Пользователь вводит данные. Сделайте проверку данных и преобразуйте если возможно в один из вариантов ниже:
* Целое положительное число
* Вещественное положительное или отрицательное число
* Строку в нижнем регистре, если в строке есть хотя бы одна заглавная буква
* Строку в верхнем регистре в остальных случаях
### [Задание 3](les_3/task_3_3.py)
Создайте вручную кортеж содержащий элементы разных типов. Получите из него словарь списков, где: ключ — тип элемента, значение — список элементов данного типа.
### [Задание 4](les_3/task_3_4.py)
Создайте вручную список с повторяющимися элементами. Удалите из него все элементы, которые встречаются дважды.
### [Задание 5](les_3/task_3_5.py)
Создайте вручную список с повторяющимися целыми числами. Сформируйте список с порядковыми номерами нечётных элементов исходного списка. Нумерация начинается с единицы.
### [Задание 6](les_3/task_3_6.py)
Пользователь вводит строку текста. Вывести каждое слово с новой строки. Строки нумеруются начиная с единицы.
Слова выводятся отсортированными согласно кодировки Unicode. Текст выравнивается по правому краю так, чтобы у самого длинного слова был один пробел между ним и номером строки.
### [Задание 7](les_3/task_3_7.py)
Пользователь вводит строку текста. Подсчитайте сколько раз встречается каждая буква в строке без использования метода count и с ним. Результат сохраните в словаре, где ключ — символ, а значение — частота встречи символа в строке. Обратите внимание на порядок ключей. Объясните почему они совпадают или не совпадают в ваших решениях.
### [Задание 8](les_3/task_3_8.py)
Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга, а значение — кортеж вещей. Ответьте на вопросы:
* Какие вещи взяли все три друга
* Какие вещи уникальны, есть только у одного друга
* Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
Для решения используйте операции с множествами. Код должен расширяться на любое большее количество друзей.

## [Домашнее задание 3](les_3/HW_3)
### [Задание 1](les_3/HW_3/task_hw_3_1.py)
Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами. В результирующем списке не должно быть дубликатов.
### [Задание 2](les_3/HW_3/task_hw_3_2.py)
В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых. Не учитывать знаки 
препинания и регистр символов. За основу возьмите любую статью из википедии или из документации к языку.
### [Задание 3](les_3/HW_3/task_hw_3_3.py)
Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. Определите какие вещи 
влезут в рюкзак передав его максимальную грузоподъёмность. Достаточно вернуть один допустимый вариант. 

## [Семинар 4 - Функции](les_4/)
### [Задание 1](les_4/task_1.py)
Напишите функцию, которая принимает строку текста. Вывести функцией каждое слово с новой строки. Строки нумеруются начиная с единицы. Слова выводятся отсортированными согласно кодировки Unicode. Текст выравнивается по правому краю так, чтобы у самого длинного слова был один пробел между ним и номером строки
### [Задание 2](les_4/task_2.py)
Напишите функцию, которая принимает строку текста. Сформируйте список с уникальными кодами Unicode каждого символа введённой строки отсортированный по убыванию.
### [Задание 3](les_4/task_3.py)
Функция получает на вход строку из двух чисел через пробел. Сформируйте словарь, где ключом будет символ из Unicode, а значением —  его порядковый номер из диапазона, границами которого являются введенные числа. Границы диапазона учитывать.
### [Задание 4](les_4/task_4.py)
Функция получает на вход список чисел. Отсортируйте его элементы in place без использования встроенных в язык сортировок. Как вариант напишите сортировку пузырьком.
### [Задание 4](les_4/task_4.1.py)
Функция получает на вход список чисел. Отсортируйте список по убыванию суммы цифр
**[Другой вариант решеения](les_4/task_4.2.py)**
### [Задание 5](les_4/task_5.py)
Функция принимает на вход три списка одинаковой длины:
* имена str, 
* ставка int, 
* премия str с указанием процентов вида «10.25%».
Вернуть словарь с именем в качестве ключа и суммой премии в качестве значения. Сумма рассчитывается как ставка умноженная на процент премии.
### [Задание 6](les_4/task_6.py)
Функция получает на вход список чисел и два индекса. Вернуть сумму чисел между переданными индексами. Если индекс выходит за пределы списка, сумма считается до конца и/или начала списка.
### [Задание 7](les_4/task_7.py)
Функция получает на вход словарь с названием компании в качестве ключа и списком с доходами и расходами (3-10 чисел) в качестве значения. Вычислите итоговую прибыль или убыток каждой компании. Если все компании прибыльные, верните истину, а если хотя бы одна убыточная — ложь.
### [Задание 8](les_4/task_8.py)
Создайте несколько переменных заканчивающихся и не оканчивающихся на «s». Напишите функцию, которая при запуске заменяет содержимое переменных, оканчивающихся на s (кроме переменной из одной буквы s) на None. Значения не удаляются, а помещаются в одноимённые переменные без s на конце.

## [Домашнее задание 4](les_4/HW_4)
### [Задание 1](les_4/HW4/task_hw_4_1.py)
Напишите функцию для транспонирования матрицы.
### [Задание 2](les_4/HW4/task_hw_4_2.py)
Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, где ключ — значение переданного аргумента, а значение — имя аргумента. Если ключ не хешируем, используйте его строковое представление
### [Задание 3](les_4/HW4/task_hw_4_3.py)
Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции. Дополнительно сохраняйте все операции поступления и снятия средств в список.

## [Сеимнар 5 - Итераторы и генераторы](les_5/)
### [Задание 1](les_5/task_1.py)
Пользователь вводит строку из четырёх или более целых чисел, разделённых символом “/”. 
Сформируйте словарь, где:
* второе и третье число являются ключами.
* первое число является значением для первого ключа.
* четвертое и все возможные последующие числа хранятся в кортеже как значения второго ключа.
### [Задание 2](les_5/task_2.py)
Самостоятельно сохраните в переменной строку текста. Создайте из строки словарь, где ключ — буква, а значение — код буквы. Напишите преобразование в одну строку.
### [Задание 3](les_5/task_3.py)
Продолжаем развивать задачу 2. Возьмите словарь, который вы получили. 
Сохраните его итераторатор. Далее выведите первые 5 пар ключ-значение, обращаясь к итератору, а не к словарю.
### [Задание 4](les_5/task_4.py)
Создайте генератор чётных чисел от нуля до 100. Из последовательности исключите числа, сумма цифр которых равна 8. 
Решение в одну строку
### [Задание 5](les_5/task_5.py)
Напишите программу, которая выводит на экран числа от 1 до 100. 
При этом вместо чисел, кратных трем, программа должна выводить слово «Fizz». Вместо чисел, кратных пяти — слово «Buzz». Если число кратно и 3, и 5, то программа должна выводить слово «FizzBuzz».
* Превратите решение в генераторное выражение, лучше многострочное (почему?)
### [Задание 6](les_5/task_6.py)
Создайте функцию-генератор. Функция генерирует N простых чисел, начиная с числа 2. Для проверки числа на простоту используйте правило: «число является простым, если делится нацело только на единицу и на себя».

## [Домашнее задание 5](les_5/HW_5)
### [Задание 1](les_5/HW5/task_hw_5_1.py)
Напишите функцию, которая принимает на вход строку - абсолютный путь до файла. Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
### [Задание 2](les_5/HW5/task_hw_5_2.py)
Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины: имена str, ставка int, премия str с указанием процентов вида “10.25%”. В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения. Сумма рассчитывается как ставка умноженная на процент премии
### [Задание 3](les_5/HW5/task_hw_5_3.py)
Создайте функцию генератор чисел Фибоначчи

## [Семинар 6 - Модули](les_6/package/)
### [Задание 2](les_6/package/task_2.py)
Создайте модуль с функцией внутри. Функция принимает на вход три целых числа: нижнюю и верхнюю границу и количество попыток. Внутри генерируется случайное число в указанных границах и пользователь должен угадать его за заданное число попыток. Функция выводит подсказки “больше” и “меньше”. Если число угадано, возвращается истина, а если попытки исчерпаны - ложь.
### [Задание 3](les_6/package/task_3.py)
Улучшаем задачу 2. Добавьте возможность запуска функции “угадайки” из модуля в командной строке терминала.
Строка должна принимать от 1 до 3 аргументов: параметры вызова функции. Для преобразования строковых аргументов командной строки в числовые параметры используйте генераторное выражение.
### [Задание 4](les_6/package/task_4.py)
Создайте модуль с функцией внутри. Функция получает на вход загадку, список с возможными верными вариантами отгадок и количество попыток на угадывание. Функция возвращает номер попытки, с которой была отгадана загадка или ноль, если попытки исчерпаны.
### [Задание 5](les_6/package/task_5.py)
Добавьте в модуль с загадками функцию, которая принимает на вход строку (текст загадки) и число (номер попытки, с которой она угадана). Функция формирует словарь с информацией о результатах отгадывания. Для хранения используйте защищённый словарь уровня модуля. Отдельно напишите функцию, которая выводит результаты угадывания из защищённого словаря в удобном для чтения виде. Для формирования результатов используйте генераторное выражение.
### [Задание 7](les_6/package/task_7.py)
Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY. Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна. Для простоты договоримся, что год может быть в диапазоне [1, 9999]. Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.
Проверку года на високосность вынести в отдельную защищённую функцию.

## [Домашнее задание 6 - Задача о 8 ферзях](les_6/package/task_hw_6.py)
Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код, решающий задачу о 8 ферзях.
Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга. Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга. Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей. Если ферзи не бьют друг друга верните истину, а если бьют - ложь.

## [Семинар 7 - Файловая система](les_7/)
### [Задание 1](les_7/task_1.py)
Напишите функцию, которая заполняет файл (добавляет в конец) случайными парами чисел.
Первое число int, второе - float разделены вертикальной чертой. Минимальное число - -1000, максимальное - +1000. Количество строк и имя файла передаются как аргументы функции.
### [Задание 2](les_7/task_2.py)
Напишите функцию, которая генерирует псевдоимена. Имя должно начинаться с заглавной буквы, состоять из 4-7 букв, среди которых обязательно должны быть гласные. Полученные имена сохраните в файл.
### [Задание 3](les_7/task_3.py)
Напишите функцию, которая открывает на чтение созданные в прошлых задачах файлы с числами и именами. Перемножьте пары чисел. В новый файл сохраните имя и произведение:
* если результат умножения отрицательный, сохраните имя записанное строчными буквами и произведение по модулю
* если результат умножения положительный, сохраните имя прописными буквами и произведение округлённое до целого.
В результирующем файле должно быть столько же строк, сколько в более длинном файле. При достижении конца более короткого файла, возвращайтесь в его начало.
### [Задание 4](les_7/task_4.py)
Создайте функцию, которая создаёт файлы с указанным расширением. Функция принимает следующие параметры:
* расширение
* минимальная длина случайно сгенерированного имени, по умолчанию 6
* максимальная длина случайно сгенерированного имени, по умолчанию 30
* минимальное число случайных байт, записанных в файл, по умолчанию 256
* максимальное число случайных байт, записанных в файл, по умолчанию 4096
* количество файлов, по умолчанию 42
Имя файла и его размер должны быть в рамках переданного диапазона.
### [Задание 5](les_7/task_5.py)
Доработаем предыдущую задачу. Создайте новую функцию которая генерирует файлы с разными расширениями. Расширения и количество файлов функция принимает в качестве параметров. Количество переданных расширений может быть любым. Количество файлов для каждого расширения различно. Внутри используйте вызов функции из прошлой задачи.
### [Задание 6](les_7/task_6.py)
Дорабатываем функции из предыдущих задач. Генерируйте файлы в указанную директорию — отдельный параметр функции. Отсутствие/наличие директории не должно вызывать ошибок в работе функции (добавьте проверки). Существующие файлы не должны удаляться/изменяться в случае совпадения имён.
### [Задание 7](les_7/task_7.py)
Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п. Каждая группа включает файлы с несколькими расширениями. В исходной папке должны остаться только те файлы, которые не подошли для сортировки.

## [Домашнее задание 7 - Групповое переименование ](les_7/task_hw_7.py)
Напишите функцию группового переименования файлов. Она должна:
* принимать параметр желаемое конечное имя файлов.
* при переименовании в конце имени добавляется порядковый номер.
* принимать параметр количество цифр в порядковом номере.
* принимать параметр расширение исходного файла. 
* переименование должно работать только для этих файлов внутри каталога. 
* принимать параметр расширение конечного файла.
* принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.

## [Семинар 8 - Сериализация](les_8/)
### [Задание 1](les_8/task_1.py)
Вспоминаем задачу 3 из прошлого семинара. Мы сформировали текстовый файл с псевдо именами и произведением чисел. Напишите функцию, которая создаёт из созданного ранее файла новый с данными в формате JSON. Имена пишите с большой буквы. Каждую пару сохраняйте с новой строки.
### [Задание 2](les_8/task_2.py)
Напишите функцию, которая в бесконечном цикле запрашивает имя, личный идентификатор и уровень доступа (от 1 до 7). После каждого ввода добавляйте новую информацию в JSON файл. Пользователи группируются по уровню доступа. Идентификатор пользователя выступает ключём для имени. Убедитесь, что все идентификаторы уникальны независимо
от уровня доступа. При перезапуске функции уже записанные в файл данные должны сохраняться.
### [Задание 3](les_8/task_3.py)
Напишите функцию, которая сохраняет созданный в прошлом задании файл в формате CSV.
### [Задание 4](les_8/task_4.py)
Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader. Дополните id до 10 цифр незначащими нулями. В именах первую букву сделайте прописной. Добавьте поле хеш на основе имени и идентификатора. Получившиеся записи сохраните в json файл, где каждая строка csv файла представлена как отдельный json словарь. Имя исходного и конечного файлов передавайте как аргументы функции.
### [Задание 5](les_8/task_5.py)
Напишите функцию, которая ищет json файлы в указанной директории и сохраняет их содержимое в виде одноимённых pickle файлов.
### [Задание 6](les_8/task_6.py)
Напишите функцию, которая преобразует pickle файл хранящий список словарей в табличный csv файл. Для тестированию возьмите pickle версию файла из задачи 4 этого семинара. Функция должна извлекать ключи словаря для заголовков столбца из переданного файла.
### [Задание 7](les_8/task_7.py)
Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader. Распечатайте его как pickle строку.

## [Домашнее задание 8 - Рекурсивный обход директории](les_8/task_hw_7.py)
Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории. Результаты обхода сохраните в файлы json, csv и pickle.
* Для дочерних объектов указывайте родительскую директорию.
* Для каждого объекта укажите файл это или директория.
* Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.

## [Семинар 9 - Декораторы](les_9/)
### [Задание 1](les_9/task_1.py)
Создайте функцию-замыкание, которая принимает два целых числа:
* от 1 до 100 для загадывания
* от 1 до 10 для количества попыток
Функция возвращает функцию, которая через консоль просит угадать загаданное число за указанное число попыток. 
### [Задание 2](les_9/task_2.py)
Дорабатываем задачу 1. Превратите внешнюю функцию в декоратор. Он должен проверять входят ли переданные в функцию-угадайку числа в диапазоны [1, 100] и [1, 10]. Если не входят, вызывать функцию со случайными числами из диапазонов.
### [Задание 3](les_9/task_3.py)
Напишите декоратор, который сохраняет в json файл параметры декорируемой функции и результат, который она возвращает. При повторном вызове файл должен расширяться, а не перезаписываться. Каждый ключевой параметр сохраните как отдельный ключ json словаря. Для декорирования напишите функцию, которая может принимать как позиционные, так и ключевые аргументы. Имя файла должно совпадать с именем декорируемой функции.
### [Задание 4](les_9/task_4.py)
Создайте декоратор с параметром. Параметр - целое число, количество запусков декорируемой функции.
### [Задание 5](les_9/task_5.py)
Объедините функции из прошлых задач. Функцию угадайку задекорируйте:
* декораторами для сохранения параметров
* декоратором контроля значений
* декоратором для многократного запуска.
Выберите верный порядок декораторов.

## [Домашнее задание 9 - Поиск корней квадратного уравнения с сохранением в csv и декораторами](les_9/task_hw_9.py)
Напишите следующие функции:
* Нахождение корней квадратного уравнения
* Генерация csv файла с тремя случайными числами в каждой строке 100-1000 строк.
* Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
* Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.

## [Семинар 10 - ООП. Начало](les_10/)
### [Задание 1](les_10/Task_1_Circle.py)
Создайте класс окружность. Класс должен принимать радиус окружности при создании экземпляра. У класса должно быть два метода, возвращающие длину окружности и её площадь.
### [Задание 2](les_10/Task_2_Rectangle.py)
Создайте класс прямоугольник. Класс должен принимать длину и ширину при создании экземпляра. У класса должно быть два метода, возвращающие периметр и площадь. Если при создании экземпляра передаётся только одна сторона, считаем что у нас квадрат.
### [Задание 3](les_10/Task_3_Human.py)
Напишите класс для хранения информации о человеке: ФИО, возраст и т.п. на ваш выбор. У класса должны быть методы birthday для увеличения возраста на год, full_name для вывода полного ФИО и т.п. на ваш выбор. 
### [Задание 4](les_10/Task_4_Staff.py)
Создайте класс Сотрудник. Воспользуйтесь классом человека из прошлого задания. У сотрудника должен быть:
* шестизначный идентификационный номер
* уровень доступа вычисляемый как остаток от деления суммы цифр id на семь
### [Задание 5](les_10/Task_5_Animals.py)
Создайте три (или более) отдельных классов животных. Например рыбы, птицы и т.п. У каждого класса должны быть как общие свойства, например имя, так и специфичные для класса. Для каждого класса создайте метод, выводящий информацию специфичную для данного класса.
### [Задание 6](les_10/Task_6_Animals.py)
Доработайте задачу 5. Вынесите общие свойства и методы классов в класс Животное. Остальные классы наследуйте от него. Убедитесь, что в созданные ранее классы внесены правки

## [Домашнее задание 10]
### [Задание 1](/les_10/HW_animals_facrory.py)
Доработаем задачи 5-6. Создайте класс-фабрику. Класс принимает тип животного (название одного из созданных классов)
и параметры для этого типа. Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.
### [Задание 2](/les_10/HW_task_3_1.py)
Возьмите любую из задач с прошлых семинаров (например сериализация данных), которые вы уже решали. Превратите функции в методы класса, а параметры в свойства. Задачи должны решаться через вызов методов экземпляра.
* * *
Создайте модуль с функцией внутри. Функция принимает на вход три целых числа: нижнюю и верхнюю границу и количество попыток. Внутри генерируется случайное число в указанных границах и пользователь должен угадать его за заданное число попыток. Функция выводит подсказки “больше” и “меньше”. Если число угадано, возвращается истина, а если попытки исчерпаны - ложь.
* * *
### [Задание 3](/les_10/HW_task_3_2.py)
Возьмите любую из задач с прошлых семинаров (например сериализация данных), которые вы уже решали. Превратите функции в методы класса, а параметры в свойства. Задачи должны решаться через вызов методов экземпляра.
Прочитайте csv файл без использования csv.DictReader. Дополните id до 10 цифр незначащими нулями. В именах первую букву сделайте прописной. Добавьте поле хеш на основе имени и идентификатора. Получившиеся записи сохраните в json файл, где каждая строка csv файла представлена как отдельный json словарь. Имя исходного и конечного файлов передавайте как аргументы функции.

## [Семинар 11 - ООП. Особенности Python](les_11/)
### [Задание 1](les_11/Task_1_My_string.py)
Создайте класс МояСтрока, где будут доступны все возможности str и дополнительно хранится имя автора строки и время создания (time.time). Добавьте к задачам 1 и 2 строки документации для классов.
### [Задание 2](les_11/Task_2_Archive.py)
Создайте класс Архив, который хранит пару свойств. Например, число и строку. При нового экземпляра класса, старые данные из ранее созданных экземпляров сохраняются в пару списков-архивов, которые также являются свойствами экземпляра. Добавьте к задачам 1 и 2 строки документации для классов.
### [Задание 4](les_11/Task_4_Archive.py)
Доработаем класс Архив из задачи 2. Добавьте методы представления экземпляра для программиста и для пользователя.
### [Задание 5](les_11/Task_5_Rectangle.py)
Дорабатываем класс прямоугольник из прошлого семинара. Добавьте возможность сложения и вычитания. При этом должен создаваться новый экземпляр прямоугольника. Складываем и вычитаем периметры, а не длинну и ширину. При вычитании не допускайте отрицательных значений
### [Задание 6](les_11/Task_6_Reactangle.py)
Доработайте прошлую задачу. Добавьте сравнение прямоугольников по площади. Должны работать все шесть операций сравнения.

## [Домашнее задание 11 - Класс Матрица](les_11/Task_HW_Matrix.py)
Создайте класс Матрица. Добавьте методы для:
* вывода на печать
* сравнения
* сложения
* *умножения матриц

## [Семинар 12 - ООП. Финал](les_12/)
### [Задание 1](les_12/Task_1_Factorial.py)
Создайте класс-функцию, который считает факториал числа при вызове экземпляра. Экземпляр должен запоминать последние k рассчитанных фаториалов. Параметр k передаётся при создании экземпляра. Добавьте метод для просмотра ранее вызываемых значений и их факториалов
### [Задание 2](les_12/Task_2_Factorial_with.py)
Создайте класс-функцию, который считает факториал числа при вызове экземпляра. Экземпляр должен запоминать последние k рассчитанных фаториалов. Параметр k передаётся при создании экземпляра. Добавьте метод для просмотра ранее вызываемых значений и их факториалов
### [Задание 3](les_12/Task_3_New_factorial.py)
Создайте класс-генератор. Экземпляр класса должен генерировать факториал числа в диапазоне от start до stop с шагом step. Если переданы два параметра, считаем step=1. Если передан один параметр, также считаем start=1.
### [Задание 4_5](les_12/Task_4_5_New_rectangle.py)
Доработайте класс прямоугольник из прошлых семинаров. Добавьте возможность изменять длину и ширину прямоугольника и встройте контроль недопустимых значений (отрицательных). Используйте декораторы свойств
### [Задание 6](les_12/Task_6_Rectangle_descriptor.py)
Изменяем класс прямоугольника. Заменяем пару декораторов проверяющих длину и ширину на дескриптор с валидацией размера.

## [Домашнее задание 12 - Класс Студент с загрузкой в csv и проверкой данных](les_12/Task_HW_Student.py)
Создайте класс студента.
* Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
* Названия предметов должны загружаться из файла CSV при создании экземпляра. Другие предметы в экземпляре недопустимы.
* Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
* Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам всех предметов вместе взятых.

## [Семинар 13 - Исключения](les_13/)
### [Задание 1](les_13/task_1.py)
Создайте функцию, которая запрашивает числовые данные от пользователя до тех пор, пока он не введёт целое или
вещественное число. Обрабатывайте не числовые данные как исключения.
### [Задание 2](les_13/task_2.py)
Создайте функцию аналог get для словаря. Помимо самого словаря функция принимает ключ и значение по умолчанию. При обращении к несуществующему ключу функция должна возвращать дефолтное значение. Реализуйте работу через обработку исключений.
### [Задание 3](les_13/task_3.py)
Создайте класс с базовым исключением и дочерние классы-исключения:
* ошибка уровня,
* ошибка доступа.
### [Задание 4](les_13/task_4.py)
Вспоминаем задачу из семинара 8 про сериализацию данных, где в бесконечном цикле запрашивали имя, личный идентификатор и уровень доступа (от 1 до 7) сохраняя информацию в JSON файл. Напишите класс пользователя, который хранит эти данные в свойствах экземпляра. Реализуйте магический метод проверки на равенство пользователей
### [Задание 5](les_13/task_5.py)
Доработайте задачи 3 и 4. Создайте класс Project, содержащий атрибуты - список пользователей проекта и админ проекта. Класс имеет следующие методы:
* Классовый метод загрузки данных из JSON-файла (из 2 задачи семинара 8)
* Метод входа в систему - требует указать имя и id пользователя. Далее метод создает пользователя и проверяет, есть ли он в списке пользователей проекта. Если пользователь присутствует в списке пользователей проекта, то пользователь, который входит получает его уровень доступа и становится администратором.
* Метод добавления пользователя в список пользователей. Если уровень пользователя меньше, чем уровень администратора, вызывайте исключение уровня доступа.
* * Метод удаления пользователя из списка пользователей проекта
* * Метод сохранения списка пользователей в JSON-файл при выходе из контекстного менеджера

## [Домашнее задание 13]
Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях.
* Напишите к ним классы исключения с выводом подробной информации.
* Поднимайте исключения внутри основного кода.
### [Задание 1](/les_13/task_hw_13_1.py)
Задача про транспонирование матриц
### [Задание 2](/les_13/task_hw_13_2.py)
Напишите функцию, которая в бесконечном цикле запрашивает имя, личный идентификатор и уровень доступа (от 1 до 7).
После каждого ввода добавляйте новую информацию в JSON файл. Пользователи группируются по уровню доступа. Идентификатор пользователя выступает ключём для имени. Убедитесь, что все идентификаторы уникальны независимо
от уровня доступа. При перезапуске функции уже записанные в файл данные должны сохраняться.
### [Задание 3](/les_13/task_hw_13_3.py)
Создайте класс прямоугольник. Класс должен принимать длину и ширину при создании экземпляра. У класса должно быть два метода, возвращающие периметр и площадь. Если при создании экземпляра передаётся только одна сторона, считаем что у нас квадрат.

## [Семинар 14 - Основы тестирования](les_14/)
### [Задание 1](les_14/task_1.py)
Создайте функцию, которая удаляет из текста все символы кроме букв латинского алфавита и пробелов. Возвращается строка в нижнем регистре.
### [Задание 2](les_14/task_2.py)
Напишите для задачи 1 тесты doctest. Проверьте следующие варианты:
* возврат строки без изменений
* возврат строки с преобразованием регистра без потери символов
* возврат строки с удалением знаков пунктуации
* возврат строки с удалением букв других алфавитов
* возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)
### [Задание 3](les_14/task_3.py)
Напишите для задачи 1 тесты unittest. Проверьте следующие варианты:
* возврат строки без изменений
* возврат строки с преобразованием регистра без потери символов
* возврат строки с удалением знаков пунктуации
* возврат строки с удалением букв других алфавитов
* возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)
### [Задание 4](les_14/task_4_test.py)
Напишите для задачи 1 тесты pytest. Проверьте следующие варианты:
* возврат строки без изменений
* возврат строки с преобразованием регистра без потери символов
* возврат строки с удалением знаков пунктуации
* возврат строки с удалением букв других алфавитов
* возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)
### [Задание 5](les_14/task_5.py)
На семинарах по ООП был создан класс прямоугольник хранящий длину и ширину, а также вычисляющую периметр, площадь и позволяющий складывать и вычитать прямоугольники беря за основу периметр. Напишите 3-7 тестов unittest для данного класса.

## [Домашнее задание 14](/les_14/hw_les_14/task_6_hw_test.py)
На семинаре 13 был создан проект по работе с пользователями (имя, id, уровень). Напишите 3-7 тестов pytest для данного проекта. Используйте фикстуры.

## [Семинар 15 - Обзор стандартной библиотеки Python](les_15/)
### [Задание 1](les_15/task_1.py)
Напишите программу, которая использует модуль logging для вывода сообщения об ошибке в файл. Например отлавливаем ошибку деления на ноль.
### [Задание 2-3](les_15/task_2_3.py)
2. На семинаре про декораторы был создан логирующий декоратор. Он сохранял аргументы функции и результат её работы в файл. Напишите аналогичный декоратор, но внутри используйте модуль logging.
3. Доработаем задачу 2. Сохраняйте в лог файл раздельно:
* уровень логирования, levelname
* дату события, asctime
* имя функции (не декоратора), function_,__name__
* аргументы вызова, args
* результат, result
### [Задание 4](les_15/task_4.py)
Функция получает на вход текст вида: “1-й четверг ноября”, “3-я среда мая” и т.п. Преобразуйте его в дату в текущем году. Логируйте ошибки, если текст не соответсвует формату.
### [Задание 5](les_15/task_5.py)
Дорабатываем задачу 4. Добавьте возможность запуска из командной строки. При этом значение любого параметра можно опустить. В этом случае берётся первый в месяце день недели, текущий день недели и/или текущий месяц.
* *Научите функцию распознавать не только текстовое названия дня недели и месяца, но и числовые, т.е. не мая, а 5.

## [Домашнее задание 15](/les_15/task_6_hw.py)
Напишите код, который запускается из командной строки и получает на вход путь до директории на ПК. Соберите информацию о содержимом в виде объектов namedtuple. Каждый объект хранит:
* имя файла без расширения или название каталога,
* расширение, если это файл,
* флаг каталога,
* название родительского каталога.
В процессе сбора сохраните данные в текстовый файл используя логирование.
