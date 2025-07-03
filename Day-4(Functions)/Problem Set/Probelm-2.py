# 2. Count vowels in a string
def vowel_counter(string):
    vowel_count = len(
        [
            i
            for i in string
            if i in ["a", "i", "e", "o", "u"] or i in ["A", "I", "E", "O", "U"]
        ]
    )
    return vowel_count
