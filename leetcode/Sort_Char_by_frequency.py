from collections import Counter
def frequencySort(s):
    result = Counter(s)
    output = []
    for i in result:
        count = result[i]
        output.append(i*count)
    output.sort(key=len,reverse = True)
    return ''.join((output))