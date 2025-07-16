#  Count word frequencies in a sentence
def freq_map(sentence):
    words = sentence.split()
    freq_map = {}
    for word in words:
        freq_map[word] = freq_map.get(word, 0) + 1
    return freq_map
