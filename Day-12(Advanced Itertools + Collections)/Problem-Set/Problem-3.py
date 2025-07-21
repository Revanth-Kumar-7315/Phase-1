# Most Common Letter using Counter()
from collections import Counter

sentence = "Hello my name is Revanth"
print(Counter(sentence).most_common(1)[0])
