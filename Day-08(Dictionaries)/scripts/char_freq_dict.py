# Count frequency of letters in a string
def char_freq_dict(string):
    freq_map = {}
    for char in string:
        freq_map[char] = freq_map.get(char, 0) + 1
    return freq_map
