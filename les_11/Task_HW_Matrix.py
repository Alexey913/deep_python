# Создайте класс Матрица. Добавьте методы для:
# ○ вывода на печать, 
# ○ сравнения, 
# ○ сложения, 
# ○ *умножения матриц

from random import randint as rnd

class Matrix:

    def __init__(self, matrix: list[list]) -> None:
        self.value = matrix
        self.length = len(matrix)
        self.heigth = len(matrix[0])


    # def __new__(cls, *args):
    #     instance = super().__new__(cls)
    #     instance.heigth = len(args)
    #     instance.length = len(args[0])
    #     instance.matrix = args
    #     return instance
    
    def __str__(self) -> str:
        return "\n".join(str(i) for i in self.value)
    
if __name__ == "__main__":
    m = Matrix([[3, 3, 3], [1,1,1], [2,2,2]])
    print(m)