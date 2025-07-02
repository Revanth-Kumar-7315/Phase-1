Number = (input("Enter a number : ")).strip()

sum_of_digits = 0

for i in Number:
    i = int(i)
    sum_of_digits += i
print(f"The sum of digits is {sum_of_digits}")
