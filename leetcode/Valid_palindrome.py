"""
🧩 2. Problem: Valid Palindrome

Link: Valid Palindrome – Easy
Goal: Check if a string is a valid palindrome (ignore cases and non-alphanumeric).
"""


def isPalindrome(s):
    s = (s.replace(" ", "")).lower()
    charecters_of_string = []
    for i in s:
        if i in "abcdefghijklmnopqrstuvwxyz0123456789":
            charecters_of_string.append(i)
    s = "".join(charecters_of_string)
    return s == s[::-1]


# We can also use a more concise approach using isalnum() to filter characters:
# def isPalindromeConcise(s):
#     s = ''.join(c.lower() for c in s if c.isalnum())
#     return s == s[::-1]
