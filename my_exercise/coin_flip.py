import random


def coin_flip():
    if random.randint(0, 1) == 0:
        return "heads"
    else:
        return "tails"


def unfair_coin_flip(probability_of_tail):
    if random.random() < probability_of_tail:
        return 'tails'
    else:
        return 'heads'


Head = 0
Tail = 0
for i in range(10000):
    if coin_flip() == 'heads':
        Head += 1
    else:
        Tail += 1
ratio = Head / Tail
print(f'Total head is {Head} and total tail is {Tail}\nThe ratio of head to tail is {ratio:.3f}')
print()


Head_tally = 0
Tail_tally = 0
for i in range(10000):
    if unfair_coin_flip(.7) == 'heads':
        Head_tally += 1
    else:
        Tail_tally += 1
ratio_ = Head_tally / Tail_tally
print(f'Total head is {Head_tally} and total tail is {Tail_tally}\nThe ratio of head to tail is {ratio_:.3f}')


def roll():
    return random.randint(1, 6)


print(roll())
