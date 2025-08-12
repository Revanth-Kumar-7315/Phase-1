# Remove duplicates without using set()
def remove_duplicates(lst):
    unique_lst = []
    for i in lst:
        if i not in unique_lst:
            unique_lst.append(i)
    return unique_lst
