def largest(lists):
    count = 0
    largest_string = ''
    for i in lists:
        if len(i) > count:
            count = len(i)
            largest_string = i
    return largest_string


s = ['rice', 'beans', 'parrot', 'elephant', 'pineapple', 'pam']
print(largest(s))