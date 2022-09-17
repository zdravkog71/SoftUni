def fibonacci():
    first_num = 0
    second_num = 1
    while True:
        yield first_num
        n = first_num + second_num
        first_num = second_num
        second_num = n


generator = fibonacci()
for i in range(1):
    print(next(generator))