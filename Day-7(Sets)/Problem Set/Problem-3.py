# Return True if two words are anagrams using sets
def are_anagrams(word1, word2):
    return set(word1) == set(word2)
