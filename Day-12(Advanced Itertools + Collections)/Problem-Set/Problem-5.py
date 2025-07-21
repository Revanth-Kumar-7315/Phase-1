#  Group Names by First Character using defaultdict
from collections import defaultdict

names = ["apple", "ball", "cat", "rat", "right", "left", "an", "a"]
names.sort(key=lambda x: x[0])
grouped = defaultdict(list)

for i in names:
    grouped[i[0]].append(i)

print(dict(grouped))
