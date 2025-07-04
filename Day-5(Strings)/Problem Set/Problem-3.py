# 3. Check if two strings are anagrams
def anagram_checker(str_1, str_2):
    str_1 = (sorted(str_1).lower()).strip()
    str_2 = (sorted(str_2).lower()).strip()
    return str_1 == str_2
