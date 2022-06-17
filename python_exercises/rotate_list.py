# using slicing
def rotate_list(list_a, num):
    list_a = (list_a[len(list_a) - num:len(list_a)] + list_a[0: len(list_a) - num])
    return list_a


a = [1, 2, 3, 4, 5]
print(rotate_list(a, 3))

# using loop


def rotate(a_list, num):
    result = []
    for i in range(len(a_list) - num, len(a_list)):
        result.append(a_list[i])

    for i in range(0, len(a_list) - num):
        result.append(a_list[i])

    return result


print(rotate(a, 1))
