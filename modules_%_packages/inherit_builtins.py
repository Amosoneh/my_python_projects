from enum import Enum, auto


class AgeGroup(Enum):
    KID = 'kid'
    ADOLESCENT = 'adolescent'
    ADULT = 'adult'


print(AgeGroup.KID.value)
print(AgeGroup.ADOLESCENT.value)
print(AgeGroup.ADULT.value)
