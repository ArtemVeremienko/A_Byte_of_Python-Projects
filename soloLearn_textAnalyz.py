# Подсчитываем сколько раз символ встречается в строке
def count_char(text, char):
    count = 0
    for c in text:
        if c == char:
            count += 1
    return count

# Открываем и читаем файл
filename = input("Enter a filename: ")
with open(filename) as f:
    text = f.read()

print(text)

# Находим какой процент текста приходится 
# на каждый из символов алфавита
for char in "abcdefghijklmnopqrstuvwxyz":
    perc = 100 * count_char(text, char) / len(text)
    print("{0} - {1}%".format(char, round(perc, 2)))
