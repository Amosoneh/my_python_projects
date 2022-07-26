# using with
# with open('hello.text', mode='w', encoding='utf-8') as file:
#
#     file.write('I love you baby\n')
#     file.write('I mean it\n')
#     file.writelines(['I am a software engineer, ', 'Do you you believe me?'])


# using normal file writing

file = open('hello.text', mode='r', encoding='utf-8')

# file.write('I love you truly baby\n')
# file.write('I mean it\n')
# file.writelines(['I am a software engineer, ', 'Do you you believe me?'])
# file.close()
#
# for i, line in enumerate(file.readlines()):
#     print(f'line {i + 1}: {line}')
#
#
# print(isinstance(4, str))
# print(type(4) == str)
#
# print(isinstance(4, str | int | float))
# print(type(4) == str or type(4) == int or type(4) == float)


lst = [1, 2, 4]


def simulate():
    try:
        # d = 4 + 'i'
        # s = lst[8]
        return 'I did well'
    except IndexError as e:
        print(f'Error occurred: {e}')
    except (TypeError, ValueError) as e:
        print(f'Error occurred: {e}')
    finally:
        print('I will run whether error or not')


simulate()
