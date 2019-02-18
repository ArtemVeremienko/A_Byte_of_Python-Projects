class Robot:
    '''Представляет робота с именем'''
    # Переменная класса, содержащая количество роботов
    population = 0

    def __init__(self, name):
        '''Инициализация данных'''
        self.name = name
        print('(Инициализация {})'.format(self.name))

        # При создании этой личности, робот добавляется
        # к переменной 'population'
        Robot.population += 1
    
    def die(self):
        '''Я умираю.'''
        print('{} уничтожается!'.format(self.name))

        Robot.population -= 1

        if Robot.population == 0:
            print('{} был последним.'.format(self.name))
        else:
            print('Осталось {:d} работающих роботов'.format(Robot.population))

    def sayHi(self):
        '''Приветствие робота.

        Да, они это могут.'''
        print('Приветсвую! Мои хозяева называют меня {}.'.format(self.name))
    
    @classmethod
    def howMany(cls):
        '''Выводит численность роботов'''
        print('У нас {:d} роботов'.format(cls.population))

droid1 = Robot('R2-D2')
droid1.sayHi()
Robot.howMany()

droid2 = Robot('C-3PO')
droid2.sayHi()
Robot.howMany()

print("\nЗдесь роботы могут проделать какую-то работу.\n")

print("Роботы закончили свою работу. Давайте уничтожим их.")

droid1.die()
droid2.die()

Robot.howMany()