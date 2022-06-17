# import itertools
# for i, j, in itertools.product(range(1, 13), range(1, 13)):
#     # print('{} x {} = {}'.format(i, j, i * j))
#     # if j == 12:
#     #     print()
#
#     print(f'{i:>5} x {j:<2} = {i*j:<5}')
#     if j == 12:
#         print()

# arr = [1, 2, 4, 3]


# def sum_even_sub_odd(array):
#     total = 0
#     for n in array:
#         if n % 2 == 0:
#             total += n
#         else:
#             total -= n
#     print(total)
#
# print(sum_even_sub_odd(arr))

# word = 'hello'
# for letter in word:
#     print(letter)
# for i in range(len(word)):
#     print(i)
#
# for i, letter in enumerate(word):
#     print(i, letter)

# how to split
# s = 'I love you so much'
# a, b, c, d, e = s.split(' ')
# print(s.split(' '))
#
# print(s.partition(' '))

def celsius_to_fahrenheit(celsius: float) -> float:
    return celsius * 1.8 + 32


fahrenheit = celsius_to_fahrenheit(100)
print(fahrenheit)
