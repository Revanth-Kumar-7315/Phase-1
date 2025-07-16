# Group elements of list by length
def group_by_length(words):
    grouped = {}
    for word in words:
        length = len(word)
        if length not in grouped:
            grouped[length] = word
        else:
            grouped[length].append(word)
    return grouped
