from datetime import datetime


def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = datetime.now()
        result = func(*args, **kwargs)
        end_time = datetime.now()
        print(f"Время выполнения функции {func.__name__}: {end_time - start_time}")
        return result
    return wrapper


@measure_time
def func1():
    print('ABCDEABCDE')


@measure_time
def func2():
    print("1234567890")


func1()
func2()
