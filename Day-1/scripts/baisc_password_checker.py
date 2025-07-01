password = input("Enter a Password : ")

if 6 < len(password) < 10:
    print("Passwords length shouldbe between 6 and 10.")
elif password.isnumeric():
    print("Password cannot be only numbers.")
else:
    print("Password looks good.")
