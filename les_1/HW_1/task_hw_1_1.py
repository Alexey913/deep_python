# Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
# Дано a, b, c — стороны предполагаемого треугольника.
# Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
# Если хотя бы в одном случае отрезок окажется больше суммы двух других,
# то треугольника с такими сторонами не существует.
# Отдельно сообщить является ли треугольник разносторонним,
# равнобедренным или равносторонним.

print("Введите длины сторон треугольника")
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
if a + b <= c or a + c <= b or b + c <= a:
    print(f"Треугольника со сторонами {a}, {b} и {c} не существует!")
elif a == b == c:
    print(f"Треугольник со сторонами {a}, {b} и {c} является равносторонним!")
elif a == b or a == c or b == c:
    print(f"Треугольник со сторонами {a}, {b} и {c} является равнобедренным!")
else:
    print(f"Треугольник со сторонами {a}, {b} и {c} является разносторонним!")
