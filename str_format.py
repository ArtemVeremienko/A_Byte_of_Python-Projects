#!/usr/bin/env python3
age = 26
name = 'Artem'

print('Возраст {0} -- {1} лет.'.format(name,age))
print('Почему {0} забавляется с этим Python?'.format(name))

# десятичное число (.) с точностью в 3 знака для плавающих:
print('{0:.3}'.format(1/3))
# заполнить подчёркиваниями (_) с центровкой текста (^) по ширине 11:
print('{0:_^11}'.format('hello'))
# по ключевым словам:
print('{name} написал {book}'.format(name='Artem', book='A Byte of Python'))