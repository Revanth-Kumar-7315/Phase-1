from collections import defaultdict

names = ["alice", "adam", "bob", "barry", "charlie"]
grouped_names = defaultdict(list)

for name in names:
    grouped_names[name[0]].append(name)

print("grouped_names")
for key, value in grouped_names.items():
    print(f"{key}:{value}")
