N = int(input("Введіть число від 1 до 100: "))
i = suma = 0

while i <= N:
    suma += i
    i += 1
print("Сума " + str(N) + " перших натуральних чисел рівна - " + str(suma))
