Username = "Revanth"
Password = 1234   

input_username = input("Enter your username: ")
input_password = input("Enter your password: ")
if input_username == Username and input_password == Password:
    print("Login successful!")
elif input_username != Username and input_password == Password:
    print("Incorrect username. Please try again.")
elif input_username == Username and input_password != Password:
    print("Incorrect password. Please try again.")
else:
    print("Both username and password are incorrect. Please try again.")