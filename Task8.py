a = int(input("Введіть ціле число: "))
next_simple_number = a + 1

while True:
    is_prime = True

    for i in range(2, int(next_simple_number ** 0.5) + 1):
        if next_simple_number % i == 0:
            is_prime = False
            break

    if is_prime:
        print("Наступне просте число: " + str(next_simple_number))
        break

    next_simple_number += 1
