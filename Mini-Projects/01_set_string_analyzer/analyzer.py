import string


def clean_text(text):
    """Remove punctuation and convert to lowercase."""
    return text.translate(str.maketrans("", "", string.punctuation)).lower()


def tokenize(text):
    """Split cleaned text into words."""
    return text.split()


def build_frequency_map(words):
    """Build a frequency map of words."""
    freq_map = {}
    for word in words:
        freq_map[word] = freq_map.get(word, 0) + 1
    return freq_map


def get_most_frequent_words(freq_map):
    """Return the most frequent word(s) and its frequency."""
    max_freq = max(freq_map.values())
    most_frequent = [word for word, count in freq_map.items() if count == max_freq]
    return most_frequent, max_freq


def find_palindromes(words):
    """Return list of palindromes with length > 1."""
    return [word for word in set(words) if word == word[::-1] and len(word) > 1]


def main():
    text = input("Enter a sentence or paragraph:\n> ")

    cleaned = clean_text(text)
    words = tokenize(cleaned)
    unique_words = set(words)

    print("\n📊 Analysis Results:")
    print(f"Total words: {len(words)}")
    print(f"Unique words: {len(unique_words)}")

    freq_map = build_frequency_map(words)
    print(f"\n🔢 Word Frequencies:\n{freq_map}")

    most_frequent, max_freq = get_most_frequent_words(freq_map)
    print(f"\n🔥 Most Frequent Word(s): {most_frequent} (Frequency: {max_freq})")

    palindromes = find_palindromes(words)
    print(f"\n🔁 Palindromes (length > 1): {palindromes if palindromes else 'None'}")


if __name__ == "__main__":
    main()
