# 2. Count vowels and consonants in a sentence
def vowel_counter(string):
    vowel_count = 0
    consonant_count = 0
    for i in string:
        if i in ["aeiouAEIOU"]:
            vowel_count += 1
        else:
            consonant_count += 1
    return f"In the string there are {vowel_count} vowels and {consonant_count} consonants."
