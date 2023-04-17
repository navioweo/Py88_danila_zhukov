def _first_func():
    '''
     функция вызывает название первой функции
    '''
    print("это первая функция")

def _second_func():
    '''
    функция вызывает название второй функции
    '''
    print("это вторая функция")

def _third_func():
    '''
    функция вызывает название третьей функции
    '''
    print("это третья функция")

def _order_func(func, n = 10):
    '''
    это функция высшего порядка которая вызывает написанные функция n раз
    '''
    for i in range(1, n + 1):
        print(f"вызов функции {func.__name__} номер {i}")
        func()



print(_first_func.__doc__)
print(_second_func.__doc__)
print(_third_func.__doc__)
_first_func()
_second_func()
_third_func()
_order_func(_first_func, 3)
print("")
_order_func(_second_func, 5)
print("")
_order_func(_third_func)
