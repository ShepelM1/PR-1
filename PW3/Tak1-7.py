# 1
def kilometers_to_miles(a):
    return a * 0.62137


# 2
def number_to_power(number, power):
    dobutok = 1
    i = 0
    while i < power:
        dobutok *= number
        i += 1
    return dobutok


# 3
def loop_factorial(number):
    res = 1
    while number > 1:
        res *= number
        number -= 1
    return res


# 4
def recursion_factorial(number):
    if number < 1:
        return 1
    else:
        return number * recursion_factorial(number - 1)


# 5
def capitalize_words(my_str):
    return " ".join([word[0].upper() + word[1:] for word in my_str.split()])


# 6
def longest_word(my_str):
    list_words = my_str.split()
    max_length = 0
    for i in list_words:
        word = len(i)
        if max_length < word:
            max_length = word
    return max_length


# 7
def word_counter(my_str):
    return len(my_str.split())


# 7
print("Кількість слів у введеному рядку - " + str(word_counter(input("Введіть рядок: "))))

# 6
# print("Найдовше слово в рядку містить " + str(longest_word(input("Введіть рядок: "))) + " символів")


# 5
# print(capitalize_words(input("Введіть рядок: ")))

# 4
# print(recursion_factorial(int(input("Введіть число: "))))

# 3
# print(loop_factorial(int(input("Введіть число: "))))

# 2
# a, b = [int(x) for x in input("Введіть число та степінь: ").split()]
# print(number_to_power(a, b))

# 1
# miles = kilometers_to_miles(float(input('Введіть кількість кілометрів: ')))
# print(miles)
