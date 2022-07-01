# def prime_num():
#     num_list = []
#     for num in range(1, 101):
#         count = 0
#         for i in range(1, num):
#             if num % i == 0:
#                 count += 1
#         if count == 1:
#             num_list.append(num)
#     return num_list
#
#
# print(prime_num())

# using list comprehension
import math


def is_prime(num: int) -> bool:
    # max_divisor = (num // 2) + 1
    if num <= 1:
        return False
    if num == 2:
        return True
    max_divisor = math.ceil(math.sqrt(num)) + 1
    for i in range(2, max_divisor):
        if num % i == 0:
            return False
    return True


def prime_number():
    num_list = []
    for i in range(1, 101):
        if is_prime(i):
            num_list.append(i)
    return num_list


print(prime_number())
print(is_prime(113))

primes = [i for i in range(1, 101) if is_prime(i)]
print(primes)

primes = {i for i in range(1, 1000) if is_prime(i)}
print(type(primes))


def cube(num: int) -> int:
    return num ** 3


cubes = [cube(i) for i in range(1, 11)]
print(cubes)

dicts = {k: v for k, v in enumerate(range(1, 10))}
print(dicts)