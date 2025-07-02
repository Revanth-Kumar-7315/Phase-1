"""
Problem 4: Remove Duplicates from a List (using loop only)

🎯 Goal: Cannot use set()
👨‍🏫 Learning: List iteration, building new list

# Input: [1,2,2,3,1,4] → Output: [1,2,3,4]
# Track with: result list + "if not in"
"""

Size_of_array = int(input(f"Enter the size of list : "))
a = []
b = []

for i in range(Size_of_array):
    while True:
        try:
            value = int(input(f"Enter the vale at {i} position : "))
            a.append(value)
            break
        except ValueError:
            print("Invalid input. Please enter a whole number.")
print("==================================")
print(f"The given list is : {a}")

for i in a:
    if i not in b:
        b.append(i)
print("==================================")
print(f"The final list is : {b}")
