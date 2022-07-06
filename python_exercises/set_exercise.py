s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}
s3 = {1, 3}
s4 = {1, 2, 3, 4, 5, 6, 7, 8}

# s1.add(9)
# s1.remove(2)
# s1.update(s2)
# s1 | s2
# s1.union(s2)
# s1 |= s2
# s1.discard(1)
# print(s1.intersection(s2))
# print(s1 & s2)
# s3.intersection_update(s4)
# s1 &= s3
# print(s1.symmetric_difference(s2))
# s1 ^ s2
# s1 ^= s2
# print(s2.difference(s1))
# print(s1)

# print(s1.isdisjoint(s2))
# print(s1 > s3)
# print(s3 < s1)

d1 = {'a': 1, 'b': 2, 'c': 3}

print(d1.values())
print(d1.keys())
print(list(d1.items()))
print(list(d1.values()))
print(list(d1.keys()))

for k in d1:
    print(k)

for key, values in d1.items():
    print(f"{key} --> {values}")
