# to append a num in a list

lst = [i for i in range(1, 11, 2)]
print(lst)
# when given a condition
lst_1 = [i for i in range(1, 11) if i % 2 == 0]
print(lst)

# if having an if-else statement, the else comes first before the loop

lst_2 = [i**2 if i % 2 == 0 else i for i in range(1, 11)]
print(lst_2)

num = [int(input(f'Enter number{i+1}: ')) for i in range(3)]
print(num)
print('Max Score = ', max(num))
print('Min Score = ', min(num))
print('Total Scores = ', sum(num))
print('Average = ', sum(num) / len(num))
