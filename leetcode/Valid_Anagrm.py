"""def isAnagram(s, t):
    if len(s) != len(t):
        return False
    freq_s = {}
    freq_t = {}
    for i in range(len(s)):
        freq_s[s[i]] = freq_s.get(s[i], 0) + 1
        freq_t[t[i]] = freq_t.get(t[i], 0) + 1
    return freq_s == freq_t
"""

from collections import Counter,deque,defaultdict
def isAnagram(s,t):
    from collections import Counter
    return Counter(s) == Counter(t)