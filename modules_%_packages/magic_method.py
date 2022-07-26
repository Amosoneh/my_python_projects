class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'I am {self.name} and i am {self.age}years old'

    def __eq__(self, other):
        return self.age == other.age

    def __lt__(self, other):
        return self.age < other.age

    def __format__(self, format_spec):
        if format_spec == 'n':
            return self.name
        else:
            return str(self)

    def __len__(self):
        return len(self.name)

    def __repr__(self):
        return f'Person({self.name}, {self.age})'


omotee = Person('Omotola', 20)
shafspecs = Person('Amos', 33)

print(f'{omotee:n}')
print(f'{shafspecs!r}')
print(f'{shafspecs!s}')
print(omotee < shafspecs)
print(len(shafspecs))
