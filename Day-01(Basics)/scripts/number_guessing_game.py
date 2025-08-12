import random

target = random.randint(0, 10)
Your_Guess = int(input("Enter your Guess = "))
print(f"Random number is {target}")

if target == Your_Guess:
    print("You guessed it right.")
else:
    print("You guessed it wrong.")
