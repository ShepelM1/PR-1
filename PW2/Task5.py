# Введення кількості рядків та стовпців
rows = int(input("Введіть кількість рядків: "))
cols = int(input("Введіть кількість стовпців: "))

# Ініціалізація матриці з нульовими значеннями
matrix = [[0] * cols for _ in range(rows)]

# Введення елементів матриці від користувача
for i in range(rows):
    for j in range(cols):
        matrix[i][j] = int(input(f"Введіть елемент матриці на позиції ({i + 1}, {j + 1}): "))

# Знаходження номерів рядка та стовпця для найбільшого та найменшого елементів
min_value = matrix[0][0]
max_value = matrix[0][0]
min_index = (0, 0)
max_index = (0, 0)

for i in range(rows):
    for j in range(cols):
        if matrix[i][j] < min_value:
            min_value = matrix[i][j]
            min_index = (i, j)
        elif matrix[i][j] > max_value:
            max_value = matrix[i][j]
            max_index = (i, j)

# Виведення результатів
print("Матриця:")
for row in matrix:
    print(row)

print(f"Найменший елемент: {min_value}, Індекс: {min_index}")
print(f"Найбільший елемент: {max_value}, Індекс: {max_index}")
