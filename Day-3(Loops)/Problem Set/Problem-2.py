"""
Problem 1: Factorial of a Number (no math module)

🎯 Goal: Loop-based multiplication
👨‍🏫 Learning: Initialization, control flow, edge cases (0!, 1!)

# Input: 5 → Output: 120
# Use: for loop version first, then while version
"""

Number = int(input("Enter a Number : "))
i = Number
fact = 1

while i > 0:
    fact *= i
    i -= 1

print(f"Factorial of {Number} is {fact}")
