"""
Problem 3: Sum of All Odd Numbers Between 1 and 100

🎯 Goal: Master range + if condition
👨‍🏫 Learning: Accumulator patterns

# Output: 1 + 3 + 5 + ... + 99
# Bonus: Use range with step = 2
"""

Starting_Number = int(input("Enter the start Number : "))
Ending_Number = int(input("Enter the end Number : "))

sum_of_odds = 0
loop_start = 0

if Starting_Number % 2 == 0:
    loop_start = Starting_Number + 1
else:
    loop_start = Starting_Number

for i in range(loop_start, Ending_Number + 1, 2):
    sum_of_odds += i

print(
    f"The sum of odd numbers from {Starting_Number } till {Ending_Number} is {sum_of_odds}"
)
