def uniqueOccurrences(List):
    counter = {}
    for i in List:
        counter[i] = counter.get(i, 0) + 1
    frequencies = list(counter.values())
    return len(frequencies) == len(set(frequencies))
