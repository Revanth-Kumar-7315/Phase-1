"""
🔁 Problem 6: Reverse a Number (no str conversion)

🎯 Goal: Use % and //
👨‍🏫 Learning: While loop, digit extraction

# Input: 123 → Output: 321
# Hints: Use %10 and //10 in loop
"""

number = int(input("Enter a number to reverse: "))
reversed_number = 0
while number > 0:
    digit = number % 10  # Get the last digit
    reversed_number = reversed_number * 10 + digit  # Build the reversed number
    number //= 10  # Remove the last digit from the original number
print("Reversed number:", reversed_number)
