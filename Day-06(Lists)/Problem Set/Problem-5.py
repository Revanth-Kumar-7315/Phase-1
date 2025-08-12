# Flatten a nested list one level deep
def flatten_once(lst):
    flat_list = []
    for item in lst:
        if isinstance(item, list):
            flat_list.extend(item)
        else:
            flat_list.append(item)
    return flat_list
