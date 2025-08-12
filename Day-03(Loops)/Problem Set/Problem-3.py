""" 
Problem 2: Count Character Frequency in a String

🎯 Goal: Use a for loop and conditionals
👨‍🏫 Learning: String iteration, counters

# Input: "hello world", char: 'l' → Output: 3
# Try with both predefined char and user input (optional)
# Use: for loop version first, then while version
# """

String = input("Enter a String : ").strip()
Identifier = input("Enter the character : ").strip()

count = 0

for i in String:
    if i == Identifier:
        count += 1
print(f"In the String {String} the charectar {Identifier} appears {count} times.")
