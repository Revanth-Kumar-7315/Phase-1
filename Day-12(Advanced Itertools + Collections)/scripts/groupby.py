from itertools import groupby

names = ["alice", "adam", "bob", "barry", "charlie"]
# Make sure to sort before using groupby
names.sort(key=lambda x: x[0])

grouped = groupby(names, key=lambda x: x[0])
for key, group in grouped:
    print(f"{key}: {list(group)}")
