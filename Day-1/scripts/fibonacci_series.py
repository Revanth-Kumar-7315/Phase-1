a, b = 0, 1
count = 0
series = []
num_terms = int(input("Enter number of terms :- "))

if num_terms <= 0:
    print(series)
elif num_terms == 1:
    series.append(a)
    print(series)
else:
    while count < num_terms:
        series.append(a)
        nth = a + b
        a = b
        b = nth
        count += 1
    print(series)
