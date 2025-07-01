"""🧪 PROBLEM 3: Multiple Conditions – Grade Classification

📝 Description:
Take a user's name, age, and marks (out of 100). Based on age and marks:

If under 18 and marks ≥ 80 → “You’re a sharp teen, NAME!”
If 18+ and marks ≥ 80 → “Well done, adulting with excellence, NAME!”
Else → “Keep learning, NAME. Progress over perfection.”
🔧 Tasks:
Validate input types (e.g., age and marks must be numbers).
Add message customization using .format() or f-strings.
"""

Name = input("Enter your Name : ")
Age = int(input("Enter your age : "))
Marks = int(input("Enter your marks : "))

if Age < 18 and Marks >= 80:
    print(f"You’re a sharp teen, {Name}!")
elif Age >= 18 and Marks >= 80:
    print(f"Well done, adulting with excellence, {Name}!")
else:
    print(f"Keep learning, {Name}. Progress over perfection")