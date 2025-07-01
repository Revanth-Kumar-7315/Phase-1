"""💡 Problem Statement:
Ask the user for the following:

Name
Age (integer)
City
Then apply this access rule:

If:
- City is "Hyderabad" (case-insensitive)
- Age > 20
- Name starts with the letter "R" (also case-insensitive)

Then → Print: "You're part of the Hyderabad Club!"

Else → Print: "Not eligible yet."

🔧 Concepts Being Tested:

Input handling (input() and int())
String methods:
.lower() or .capitalize() for case insensitivity
.startswith("R") for name check
if + and conditions (logical operators)
Defensive programming (clean inputs)

🔍 Extra Suggestions to Stand Out:

Use .strip() to clean whitespace
Normalize input for comparison (e.g., city.lower() == 'hyderabad')
Use f-strings to include name in the response
Optionally wrap logic in a function like check_eligibility()
"""
def check_eligibility():
    name = input("Enter your name: ").strip()
    age = int(input("Enter your age: ").strip())
    city = input("Enter your city: ").strip()

    if city.lower() == "hyderabad" and age > 20 and name.lower().startswith("r"):
        print("You're part of the Hyderabad Club!")
    else:
        print("Not eligible yet.")
if __name__ == "__main__":
    check_eligibility()