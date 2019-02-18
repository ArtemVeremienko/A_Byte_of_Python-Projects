#!/usr/bin/env python3

from abc import *

class SchoolMember(metaclass = ABCMeta):
    '''Представляет любого человека в школе.'''
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(Создан SchoolMember: {})'.format(self.name))
    
    @abstractmethod
    def tell(self):
        '''Вывести информацию.'''
        print('Имя: "{}" Возраст:"{}"'.format(self.name, self.age), end=" ")

class Teacher(SchoolMember):
    '''Представляет преподавателя.'''
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('(Создан Teacher: {})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Зарплата: "{}"'.format(self.salary))

class Student(SchoolMember):
    '''Представляет студента'''
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('( Создан Student: {})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Оценки: "{:d}"'.format(self.marks))

t = Teacher('Mrs. Shviridova', 40, 30000)
s = Student('Swaroop', 25, 75)

# m = SchoolMember('abc', 10)
# Это приведёт к ошибке: "TypeError: Can't instantiate abstract class"
# SchoolMember with abstract methods tell"

print() # печатает пустую строку

members = [t, s]
for member in members:
    member.tell() # работает как для преподавателя, так и для студента