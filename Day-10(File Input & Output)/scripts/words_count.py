# Count how many words are in a file
import string


def word_counter(filename):
    with open(filename, "r") as f:
        content = f.read()
        translator = str.maketrans("", "", string.punctuation)
        cleaned_text = content.translate(translator)
        words = cleaned_text.split()
        return len(words)


if __name__ == "__main__":
    filename = "Main.txt"
    print(f"Total words: {word_counter(filename)}")
