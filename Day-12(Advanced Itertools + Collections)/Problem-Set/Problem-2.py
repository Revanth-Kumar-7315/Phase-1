#  Group Words by Length using groupby()
from itertools import groupby

words = ["apple", "ball", "cat", "rat", "right", "left", "an", "a"]
words.sort(key=len)

grouped_words = groupby(words, key=len)
for key, group in grouped_words:
    print(f"{(key)}: {list(group)}")
