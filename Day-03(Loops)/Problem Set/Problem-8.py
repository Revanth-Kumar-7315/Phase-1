"""
🔁 Problem 7: Count Digits in a Number

🎯 Goal: No len(str())
👨‍🏫 Learning: Loop until number becomes 0

# Input: 140 → Output: 3
# Test with 0, 1, 100000
"""

number = int(input("Enter a number to count digits: "))
count = 0
if number == 0:
    count = 1  # Special case for 0
else:
    while number > 0:
        number //= 10  # Remove the last digit
        count += 1  # Increment count for each digit
print("Number of digits:", count)
