# ✔ Напишите функцию для транспонирования матрицы

# def transopse_matrix(size_matrix: int, list_matrix: list) -> list:
#     for i in range(size_matrix):
#         for j in range(i, size_matrix):
#             if i != j:
#                 list_matrix[i][j], list_matrix[j][i] = list_matrix[j][i], list_matrix[i][j]
#     return list_matrix


# def print_matrix(list_matrix: list):
#     for i in range(len(list_matrix)):
#         print(list_matrix[i])


# def input_matrix(size_matrix: int) -> list:
#     list_matrix = []
#     i = 0
#     while i < size_matrix:
#         string_matrix = map(int, input(f"Введите {size_matrix} элемента(ов) {i+1} строки через пробел: ").split())
#         list_matrix.append(list(string_matrix))
#         i += 1
#     return list_matrix


# size_matrix = int(input("Введите размерность матрицы: "))
# matrix = input_matrix(size_matrix)
# print("Введенная матрица:")
# print_matrix(matrix)
# transopse_matrix(size_matrix, matrix)
# print("Транспонированная матрица:")
# print_matrix(matrix)


def transopse_matrix(list_matrix: list) -> list:
    return_matrix = []
    for item in zip(*list_matrix):
        return_matrix.append(list(item))
    return return_matrix


def print_matrix(list_matrix: list):
    for i in range(len(list_matrix)):
        print(list_matrix[i])


def input_matrix(length_matrix: int, weigth_matrix: int) -> list:
    list_matrix = []
    for i in range(weigth_matrix):
        string_matrix = map(int, input(f"Введите {length_matrix} элемента(ов) {i+1} строки через пробел: ").split())
        list_matrix.append(list(string_matrix))
    return list_matrix


length, weigth = map(int, input("Введите длину и высоту матрицы через пробел: ").split())
matrix = input_matrix(length, weigth)
print("Введенная матрица:")
print_matrix(matrix)
new_matrix = transopse_matrix(matrix)
print("Транспонированная матрица:")
print_matrix(new_matrix)