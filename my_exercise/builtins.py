from functools import reduce
import operator
lst = [1, 2, 3, 4, 5, 8]
# print(all(i for i in lst if i >= 7))
# print(all(True if i >= 7 else False for i in lst))

abu = [90, 90, 70, 78]
ab = [96, 60, 80, 98]
au = [99, 68, 50, 88]
# print(list(zip(abu, ab, au)))


def longest(lst: list, num: int):
    if num > len(lst) or len(lst) == 0:
        return ""
    list_ = []
    for i in range(num):
        list_.append(lst[i:])
    return max(("".join(j) for j in zip(*list_)), key=len)
    # return max(("".join(j) for j in zip(*(lst[i:] for i in range(num)))), key=len)


# print(longest(['love', 'life', 'and', 'live', 'free', 'because', 'tomorrow', 'is', 'not', 'assured'], 3))


list_of_numbers = [1, 2, 3, 4, 5]
mapped_list = map(lambda x: x**2, list_of_numbers)
# print(list(mapped_list))
# print(list(mapped_list))

list_of_dict = [{'name': 'Asake', 'gender': 'F'}, {'name': 'Boyo', 'gender': 'M'}]

mapped_list_of_dict = list(map(lambda x: ('Mr. ' if x['gender'] == 'M' else 'Mrs. ') + x['name'], list_of_dict))
print(mapped_list_of_dict)
print([('Mr. ' if x['gender'] == 'M' else 'Mrs. ') + x['name'] for x in list_of_dict])

filtered_list_of_dict = list(filter(lambda x: x['gender'] == 'M', list_of_dict))
print(filtered_list_of_dict)
print([name for name in list_of_dict if name['gender'] == 'F'])

sum_reduce = reduce(lambda acc, val: acc + val, list_of_numbers)
sum_reduce2 = reduce(operator.add, list_of_numbers)


print(sum_reduce)
print(sum_reduce2)

fruits = ['pear', 'cucumber', 'water m', 'banana']

print(reduce(lambda x, y: x if len(x) >= len(y) else y, fruits))

