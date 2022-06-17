import string

# cipher message
# s = 'hello'
# print(s[-2:])
# #
# abc = string.ascii_lowercase
# a = 'hello can I have your number'
# key = 5
# transform = abc[key:] + abc[:key]
# x = a.translate(str.maketrans(abc, transform))
# print(x)
#
# #decipher
# z = x.translate(str.maketrans(transform, abc))
# print(z)

# word = input('Enter the word to encode: ')
# while not word.isalpha():
#     word = input('Enter the word to encode: ')
#
# key = input('Enter the cipher key: ')
# while not key.isdigit():
#     key = input('Enter the cipher key: ')
#
# if word.isalpha() and key.isdigit():
#     key_code = int(key)
#     abc = string.ascii_lowercase
#     transform = abc[key_code:] + abc[:key_code]
#     cipher = word.translate(str.maketrans(abc, transform))
#     decipher = cipher.translate(str.maketrans(transform, abc))
# print(cipher)
# print(decipher)

# for i in range(1, 13):
#     print('{} Multiplication Table'.format(i))
#     for j in range(1, 13):
#         print('{:3} x {:<3}= {:>3}'.format(i, j, j * i))
#     print('')
#
# float = 0.0000009845
# print('Float is {:<5.3e}'.format(float))


def prime_num():
    num_list = []
    for num in range(1, 101):
        count = 0
        for i in range(1, num):
            if num % i == 0:
                count += 1
        if count == 1:
            num_list.append(num)
    return num_list


print(prime_num())






