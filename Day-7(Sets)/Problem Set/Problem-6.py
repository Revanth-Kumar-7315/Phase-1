# Given a list of words, return how many are palindromes.
def palindromes_in_set(A):
    return sum([1 for word in A if word == word[::-1]])
