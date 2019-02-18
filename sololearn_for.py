words = ['hello', 'world', 'spam', 'eggs']
counter = 0
max_index = len(words) - 1

while counter <= max_index:
    word = words[counter]
    print(word + '!')
    counter += 1

hw = 'Hello, World!'
print(hw[0])

for word in words:
    print(word + '!')


for i in range(5):
    print('Hello, World!')

for i in range(5, 20, 3):
    print(i)
