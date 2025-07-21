from itertools import product, permutations, combinations

chars = ["a", "b", "c"]
print("Cartesian Product: (repetation allowed)")
for i in product(chars, repeat=3):
    print("".join(i))
print("=================================================")
print("\nPermutations: (repetation not allowed)")
for i in permutations(chars, 3):
    print("".join(i))
print("=================================================")
print("\nCombinations: (repetation not allowed)")
for i in combinations(chars, 2):
    print("".join(i))
