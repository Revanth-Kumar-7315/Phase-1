# Given two lists of numbers, return the elements common to both (use sets internally).
def common_elements(A, B):
    return set(A).intersection(set(B))
