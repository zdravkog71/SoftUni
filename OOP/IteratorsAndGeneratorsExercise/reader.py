def read_next(*args):
    index = 0
    while index < len(args):
        for el in args[index]:
            yield el
        index += 1

for i in read_next("Need", (2, 3), ["words", "."]):
    print(i)