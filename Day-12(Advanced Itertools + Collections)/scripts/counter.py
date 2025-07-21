from collections import Counter

# Example usage of Counter
words = ["apple", "banana", "apple", "orange", "banana", "apple"]
word_count = Counter(words)
print(word_count)
print("Most common word:", word_count.most_common(1))
