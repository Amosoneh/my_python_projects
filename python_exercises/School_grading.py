num_students = int(input('Enter number of students: '))
num_of_subjects = int(input('Enter number of subject: '))
count = 0
students_list = []
subject_list = [input(f'Enter subject {i + 1}: ') for i in range(num_of_subjects)]

while count != num_students:
    name = input('Enter student name: ')
    subject_scores = [int(input(f"Enter {name}'s score for {subject_name}: ")) for subject_name in subject_list]
    total = sum(subject_scores)
    avg = total / num_of_subjects
    student = {
        'name': name,
        'subject scores': subject_scores,
        'total': total,
        'average': avg
    }
    students_list.append(student)
    count += 1
    print()

average_scores = [i['average'] for i in students_list]
total_scores = [i['total'] for i in students_list]
student_name = [i['name'] for i in students_list]
scores = [i['subject scores'] for i in students_list]


def prt(a: list):
    for i in a:
        print(f'{i:>8}', end='')
    pass


pos = []
for i in total_scores:
    cou = 1
    for j in total_scores:
        if j > i:
            cou += 1
        else:
            cou = 1
        pos.append(cou)

print('=' * 40 + '\n' '\tWELCOME TO SEMICOLON AFRICA\n''312 Harbert Macaulay Road, Sabo, Yaba\n' +'=' * 40)
print(f'Natives', end=' ')
for i in subject_list:
    print(f'{i:>7}', end=' ')
a, b, c = 'Tot', 'Avg', 'Pos'
print(f'{a:>7} {b:>7}{c:>7}')
for i in range(0, len(students_list)):
    print(f'{student_name[i]}', end='')
    prt(scores[i])
    print(f'{total_scores[i]:>8} {average_scores[i]:>7}{pos[i]}')
