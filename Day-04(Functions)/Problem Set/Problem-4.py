# 4. Return only unique values from a list
def unq_values_in_list(a):
    unq_list = []
    for i in a:
        if i in unq_list:
            continue
        else:
            unq_list.append(i)
    return unq_list
