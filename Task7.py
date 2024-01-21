a, b = map(int, input("Введіть початок та кінець діапазону (через пробіл): ").split())
list_simple_numbers = []
k = 0

for i in range(a, b+1):
    for j in range(2, i):
        if i % j == 0:
            k = k + 1
    if k == 0:
        list_simple_numbers.append(i)
    else:
        k = 0
print(list_simple_numbers)
