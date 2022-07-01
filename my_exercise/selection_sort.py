from my_exercise.find_smallest import find_smallest


def selection_sort(arr):
    new_arr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr


print(selection_sort([3, 5, 7, 0, 1, -5]))
