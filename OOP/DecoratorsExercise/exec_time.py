from time import time


def exec_time(func):
    def wrappper(*args):
        start = time()
        result = func(*args)
        end = time()
        with open('./time_log.txt', 'a') as file:
            file.write(f'{func.__name__} was executed with params {args}. Elapsed time: {end - start}')
            file.write('\n')

        return result
    return wrappper


@exec_time
def loop(start, end):
    total = 0
    for x in range(start, end):
        total += x
    return total
print(loop(1, 10000000))