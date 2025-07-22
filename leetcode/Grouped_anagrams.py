from collections import defaultdict
def groupAnagrams(strs):
    block = defaultdict(list)
    for word in strs:
        block[''.join(sorted(word))].append(word)
    return list(block.values())