from functools import wraps


def logged(func):
    @wraps(func)
    def wrapper(*args):
        result = func(*args)
        resul_to_return = f'you called {func.__name__}{args}\n'
        resul_to_return += f'it returned {result}'
        return resul_to_return

    return wrapper


@logged
def func(*args):
    return 3 + len(args)



@logged
def sum_func(a, b):
    return a + b


print(sum_func(1, 4))
print(func(4, 4, 4))