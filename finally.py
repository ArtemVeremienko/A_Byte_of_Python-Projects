import time

try:
    f = open('poem.txt')
    while True: # наш обычный способо читать файлы
        line = f.readline()
        if len(line) == 0:
            break
        print(line, end='')
        time.sleep(2) # пусть подождёт некоторое время
except KeyboardInterrupt:
    print('!! Вы отменили чтение файла')
finally:
    f.close()
    print('(Очистка: Закрытие файла)')

with open('poem.txt') as f:
    for line in f:
        print(line, end='')
        time.sleep(1)