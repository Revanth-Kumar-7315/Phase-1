# Q3. String Reverser
# Take a string input and print it reversed.
# Bonus: Also print the length of the string.

String = input("Enter a String : ")

reversed_string = String[::-1]  # slicing trick

print("Reversed string:", reversed_string)
print("Length of string:", len(String))
