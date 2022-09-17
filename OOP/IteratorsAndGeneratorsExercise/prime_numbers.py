def is_prime(num):
    if num <= 1:
        return False
    result = True

    for i in range(2, num):
        if num % i == 0:
            result = False
            return result
    return result


def get_primes(integers):
    for num in integers:
        if is_prime(num):
            yield num

    # index = 0
    # numbers = [2,3,4,5,6,7,8,9]
    # is_prime = False
    #
    # while index < len(integers):
    #     for num in numbers:
    #         if not (integers[index] == 1 or num == integers[index]):
    #             if integers[index] % num == 0:
    #                 is_prime = False
    #                 break
    #             else:
    #                 is_prime = True
    #
    #     if is_prime:
    #         is_prime = False
    #         yield integers[index]
    #
    #     index += 1


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))