# 7. Return only unique words from a sentence
def unique_words(string):
    string = string.split()
    unique_words = []
    for i in string:
        if i not in unique_words:
            unique_words.append(i)
    return f"Unique words are {unique_words}"
