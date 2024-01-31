txt = input("Введіть речення: ")
words = txt.split(' ')
reversed_words = [word[::-1] for word in words]
new_txt = ' '.join(reversed_words)

print("Результат:", new_txt)
