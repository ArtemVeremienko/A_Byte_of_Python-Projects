import sys

print('Аргументы командной строки:')
for i in sys.argv:
    print(i)

print('\n\n Переменная PYTHONPATH содержит', sys.path, '\n')

import os
print(os.getcwd())