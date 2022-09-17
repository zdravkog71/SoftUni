def even_parameters(func):

    def is_even(num):
        if not isinstance(num, int):
            return False
        return num % 2 == 0


    def wrapper(*args):
        even = True
        for el in args:
            if not is_even(el):
                even = False

        if even:
            result = func(*args)
            return result

        return 'Please use only even numbers!'

    return wrapper

@even_parameters
def add(a, b):
    return a + b

print(add(2, 4))
print(add("Peter", 1))

@even_parameters
def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result

print(multiply(2, 4, 6, 8))
print(multiply(2, 4, 9, 8))