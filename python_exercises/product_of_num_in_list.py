def product(lists):
    result = 0
    for i in lists[:1]:
        result = i
        for index in lists[1:]:
            result *= index
    return result


a = [4, 2, 3, 10]
print(product(a))
print(a[:1])



