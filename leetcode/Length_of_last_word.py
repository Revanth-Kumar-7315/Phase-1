def lengthOfLastWord(s):
    words = (s.strip()).split()
    return len(words[-1])
