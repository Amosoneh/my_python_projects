def anagram(num):
    # num = int(input('Enter a number to check if its an anagram: '))
    num_squared = str(num * num)
    lem = len(num_squared)
    if str(num) == num_squared[lem - 1] or str(num) == num_squared[-2:] or str(num) == num_squared[-3:]:
        return 'This number is an anagram'
    else:
        return 'This number is not an anagram'


# anagram()
anagram_list = []
for i in range(1, 1001):
    if anagram(i) == 'This number is an anagram':
        anagram_list.append(i)

print(anagram_list)
