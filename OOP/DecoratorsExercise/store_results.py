from functools import wraps


def store_results(func):
    @wraps(func)
    def wrapper(*args):
        result = func(*args)
        with open('./result.txt', 'a') as file:
            file.write(f'Function {func.__name__} was add called. Result: {result}')
            file.write('\n')
        return result

    return wrapper


@store_results
def add(a, b):
    return a + b

@store_results
def mult(a, b):
    return a * b

add(2, 2)
mult(6, 4)


