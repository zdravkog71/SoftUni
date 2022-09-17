from itertools import permutations

def possible_permutations(seq):
    for result in permutations(seq):
        yield list(result)



[print(n) for n in possible_permutations([1, 2, 3])]