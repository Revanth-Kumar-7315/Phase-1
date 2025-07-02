"""
roblem 5: Pattern Print – Increasing Triangle

🎯 Goal: Nested loops
👨‍🏫 Learning: Outer vs inner loop logic

# Input: 5 → Output:
# *
# **
# ***
# ****
# *****
"""

Size_of_array = int(input(f"Enter the size of triangle : "))
for i in range(1, Size_of_array + 1):
    for j in range(i):
        print("*", end="")
    print()
