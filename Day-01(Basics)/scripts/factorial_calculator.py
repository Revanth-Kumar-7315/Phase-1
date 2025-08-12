Number = int(input("Enter a number : "))
answer = 1
if Number <= 0:
    print("Not possible")
elif Number == 0:
    print(1)
else:
    for i in range(1, Number + 1):
        answer *= i
        i += 1
    print(answer)
