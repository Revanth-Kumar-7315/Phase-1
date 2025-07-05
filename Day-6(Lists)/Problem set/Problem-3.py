# Find the second-largest number
def second_largest(lst):
    for i in lst:
        if lst.count(i) > 1:
            lst.remove(i)
    sorted_list = sorted(lst)
    return sorted_list[-2]
