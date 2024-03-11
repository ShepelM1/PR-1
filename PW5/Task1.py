class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        result = ""
        for row in self.matrix:
            result += " ".join(map(str, row)) + "\n"
        return result

    def __add__(self, other):
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            raise ValueError("Matrix dimensions do not match")
        result = []
        for i in range(len(self.matrix)):
            result.append([])
            for j in range(len(self.matrix[0])):
                result[i].append(self.matrix[i][j] + other.matrix[i][j])
        return Matrix(result)

    def __sub__(self, other):
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            raise ValueError("Matrix dimensions do not match")
        result = []
        for i in range(len(self.matrix)):
            result.append([])
            for j in range(len(self.matrix[0])):
                result[i].append(self.matrix[i][j] - other.matrix[i][j])
        return Matrix(result)

    def __mul__(self, other):
        if len(self.matrix[0]) != len(other.matrix):
            raise ValueError("Number of columns in the first matrix"
                             " must be equal to the number of rows in the second matrix")
        result = []
        for i in range(len(self.matrix)):
            result.append([])
            for j in range(len(other.matrix[0])):
                sum = 0
                for k in range(len(other.matrix)):
                    sum += self.matrix[i][k] * other.matrix[k][j]
                result[i].append(sum)
        return Matrix(result)


matrix1 = Matrix([[1, 2], [3, 4]])
matrix2 = Matrix([[5, 6], [7, 8]])

print("Matrix 1:")
print(matrix1)
print("Matrix 2:")
print(matrix2)

print("Addition:")
print(matrix1 + matrix2)

print("Subtraction:")
print(matrix1 - matrix2)

print("Multiplication:")
print(matrix1 * matrix2)
