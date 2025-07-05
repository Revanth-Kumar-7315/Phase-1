# Append 3 elements to a list
def append_elements(elements, given_list=[]):
    if len(elements) > 3:
        return "Please only give three elements in the list"
    else:
        for i in elements:
            given_list.append(i)
        return given_list
