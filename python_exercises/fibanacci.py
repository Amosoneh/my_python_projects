def fibonacci(n):
    a, b = 0, 1
    count = 0
    if n < 0:
        print('Incorrect input')
    elif n == 1:
        print(a)
    else:
        while count < n:
            print(a, end=" ")
            nth = a + b
            a = b
            b = nth
            count += 1


fibonacci(9)
