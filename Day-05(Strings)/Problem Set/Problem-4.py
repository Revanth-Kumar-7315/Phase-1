# 4. Return the longest word in a sentence
def longest_word(string):
    longest_word = " "
    list_of_words = string.split()
    for i in list_of_words:
        if len(i) > len(longest_word):
            longest_word = i
    return f"{longest_word} is the longest word in the string"
