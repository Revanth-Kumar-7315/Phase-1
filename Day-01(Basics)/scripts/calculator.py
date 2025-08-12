x = int(input("Enter a number = "))
y = int(input("Enter a number = "))

print(f"Sum = {x+y}")
print(f"Difference = {x-y}")
print(f"Product = {x*y}")

if y != 0:
    print(f"Divisor = {x/y}")
else:
    print("Division not possible")
