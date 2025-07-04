# 1. Check if a string is a palindrome
def palindrome_checker(string):
    string = (string.lower()).strip()
    reversed_string = string[::-1]
    return string == reversed_string
