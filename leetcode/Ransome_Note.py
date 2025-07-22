"""def canConstruct(ransomNote, magazine):
    freq_m = {}
    freq_r = {}
    for i in ransomNote:
        freq_r[i] = freq_r.get(i, 0) + 1

    for i in magazine:
        freq_m[i] = freq_m.get(i, 0) + 1

    for i in ransomNote:
        if i not in freq_m or freq_r[i] > freq_m[i]:
            return False
    return True
"""
from collections import Counter
def canConstruct(ransomNote,magazine):
    a = dict(Counter(ransomNote))
    b = dict(Counter(magazine))
    for i in a:
        if i not in b or a[i] > b[i] :
            return False
        else:
            continue
    return True
