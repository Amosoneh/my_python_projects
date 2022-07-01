# def disemvowel(string_):
#     new = []
#     d = ""
#     for a in string_:
#         if a not in "aeiouAEIOU":
#             new.append(a)
#     for s in new:
#         d += s
#     return d
#
#
def remove_vowel(string__):
    lst = [i for i in string__]
    ss = ''
    for a in lst:
        if a in "aeiouAEIOU":
            lst.remove(a)
    for s in lst:
        ss += s
    return ss
#
#
# def square_digits(num):
#     new = ""
#     for n in str(num):
#         new += str(int(n) ** 2)
#     return int(new)
#
#
# print(square_digits(9119))
# print(remove_vowel("i am new to python"))


def high_and_low(numbers):
    sum = [int(x) for x in numbers.split(' ')]
    return str(max(sum)) + ' ' + str(min(sum))
    # sum.sort()
    # length = len(sum)
    # largest = str(sum[length - 1])
    # smallest = str(sum[0])
    # return largest + " " + smallest



def find_len(list1):
    length = len(list1)
    list1.sort()
    print("Largest element is:", list1[length - 1])
    print("Smallest element is:", list1[0])
    print("Second Largest element is:", list1[length - 2])
    print("Second Smallest element is:", list1[1])


# Driver Code
# list1 = [12, 45, 2, 41, 31, 10, 8, 6, 4]
# Largest = find_len(list1)

a = "8 3 -5 42 -1 0 0 -9 4 7 4 -4"
print(high_and_low(a))
# print(sorted(("8 3 -5 42 -1 0 0 -9 4 7 4 -4").split(" ")))


hello_str ='hello world';print(hello_str[0:11:2])
print(ord('a'))
print(chr(97))
