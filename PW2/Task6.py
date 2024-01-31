txt = input("Введіть рядок: ")
char_count = {}
for char in txt:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1
for char, count in char_count.items():
    print(f"Символ '{char}' входить {count} разів")
