# Remove an element from list
def remove_element(given_list, element):
    if given_list == []:
        return "Please give atleast one element in the list"
    elif element not in given_list:
        return "Please give an element present in the list"
    else:
        given_list.remove(element)
        return given_list
