# Filter out palindromes from a list of words using filter()
def pal_or_not(lst):
    return list(filter(lambda a: a == a[::-1], lst))
