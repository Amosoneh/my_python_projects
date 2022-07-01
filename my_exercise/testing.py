def tell_me_more_about(a_language: str) -> str:
    languages = ('Java', 'Python', 'JavaScript', 'Database')

    assert a_language in languages, f"Language '{a_language}' not found"

    return a_language


print(tell_me_more_about('Java'))
print(tell_me_more_about('Go lang'))


# space complexity(constant), time complexity (0(n*n))
def two_sum(lst: list, target: int) -> list:
    for i in range(len(lst) - 1):
        for j in range(i+1, len(lst)):
            result = lst[i] + lst[j]
            if result == target:
                return [i, j]
    return []


print(two_sum([3, 8, 3, -8], 0))


# space complexity(0(n), time complexity (0(n))
def tw_sm(list_of_numbers: list, target: int) -> list | int:
    map_ = {}
    for i in range(len(list_of_numbers)):
        complement = target - list_of_numbers[i]
        if complement in map_:
            return [map_[complement], i]
        else:
            map_[list_of_numbers[i]] = i

    return -1




print(tw_sm([3, 8, 3, -8], 6))
