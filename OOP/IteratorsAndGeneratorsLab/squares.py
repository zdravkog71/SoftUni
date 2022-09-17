def squares(n):
    index = 1

    while index < n + 1:
        yield index * index
        index += 1

print(list(squares(5)))
