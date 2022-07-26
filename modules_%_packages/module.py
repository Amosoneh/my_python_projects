__all__ = ['add', 'sub']

from statistics import mean, median


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


if __name__ == "__main__":
    print('I am invisible to other modules')
    print("module:", __name__)
    print(add(4, 9))

universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]

# b = sum([i[1] for i in universities])
# print(b)


def median_num(lst: list):
    return median(lst)


def mean_number(lst: list):
    return mean(lst)


def enrollment(lst: list):
    a = [i[1] for i in lst]
    b = [i[2] for i in lst]
    return a, b


# def enrollment_state():
    # university = []
    # list_of_universities = []
    # annual_tuition_fees = ""
    # total_no_enrolled = ""
    # name_of_uni = [input('Enter school name : ')]
    # while name_of_uni != "0":
    #     total_no_enrolled = [int(input('Enter total number enrolled: '))]
    #     annual_tuition_fees = [int(input('Enter annual tuition fees: '))]
    #     name_of_uni = input('Enter school name or 0 to stop: ')
    #     university.append(name_of_uni)
    #     university.append(total_no_enrolled)
    #     university.append(annual_tuition_fees)
    # list_of_universities.append(university)
    # total_student = sum([i[1] for i in universities])
    # print(total_student)
    # total_tuition = sum([i[2] for i in universities])
    # print(total_tuition)
    # print(f'Total Student: {total_student:,} \nTotal Tuition: ${total_tuition:,}')


total_students, total_tuition = enrollment(universities)
print(f'Total Student: {sum(total_students):,} \nTotal Tuition: ${sum(total_tuition):,}')
print(f'Student Mean: {mean_number(total_students):,.2f} \nStudents Median: ${median_num(total_students):,}')
print(f'Tuition Mean: {mean_number(total_tuition):,.2f} \nTuition Median: ${median_num(total_tuition):,}')


