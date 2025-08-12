"""🧪 PROBLEM 2: BMI Calculator with Category

📝 Description:
Ask user for weight (kg) and height (cm). Convert height to meters and compute:

BMI = weight/height^2
Then, categorize:

<18.5: Underweight
18.5–24.9: Normal
25–29.9: Overweight
30+: Obese
🔧 Tasks:
Validate that height and weight are > 0.
Round BMI to 2 decimal places.
Print: "Your BMI is X and you are Y."""

Height = float(input("Enter your height (in meters) : "))
Weight = float(input("Enter your Weight (in kgs) : "))

BMI = (Weight) / (Height**2)
BMI = round(BMI, 2)
if Height <= 0 and Weight <= 0:
    print("Not Possible!")
elif BMI <= 18.5:
    print(f"Your BMI is {BMI}")
    print("You are Underweight")
elif 18.5 < BMI <= 24.9:
    print(f"Your BMI is {BMI}")
    print("You are Normal")
elif 24.9 < BMI <= 29.9:
    print(f"Your BMI is {BMI}")
    print("You are Overweight")
else:
    print(f"Your BMI is {BMI}")
    print("You are Obese")
