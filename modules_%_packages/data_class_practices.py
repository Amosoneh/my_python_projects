# class Human:
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender

from dataclasses import dataclass, field


@dataclass#(init=False)
class Human:
    name: str
    age: int
    gender: str
    children: list[str] = field(default_factory=lambda: [], init=False, repr=False)


human = Human('Amos', 22, 'M')
# human.name = 'Amos'
# human.age = 44
# human.gender = 'M'

print(human)
