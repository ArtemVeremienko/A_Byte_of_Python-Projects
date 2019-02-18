x = 30
print('x равно', x)

def func_outer():
    x = 2
    print('x равно', x)

    def func_inner():
        nonlocal x
        x = 5
    
    func_inner()
    print('Локальное х сменилось на', x)

func_outer()
print('x равно', x)