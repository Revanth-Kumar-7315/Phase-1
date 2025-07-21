def singleNumber(lst):
    for i in lst:
        if lst.count(i) == 1:
            return i
