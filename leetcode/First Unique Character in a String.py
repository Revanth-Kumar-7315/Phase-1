from collections import Counter,deque,defaultdict
def firstUniqChar(s):
    a = dict(Counter(s))
    Index = len(s)+1
    for i in a:
        if a[i] == 1:
            if s.index(i) < Index:
                Index = s.index(i)
    return Index if Index != len(s) + 1 else -1

"""def firstUniqChar(s):
    a = dict(Counter(s))
    for index,char in enumerate(s):
        if a[char] == 1:
            return index
    return -1"""