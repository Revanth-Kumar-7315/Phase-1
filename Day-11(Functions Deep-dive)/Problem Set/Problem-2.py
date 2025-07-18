# Use map() and lambda to add two lists element-wise.
def add_lists(list1, list2):
    if len(list1) != len(list2):
        return False
    else:
        add = lambda a, b: a + b
        return list(map(add, list1, list2))
