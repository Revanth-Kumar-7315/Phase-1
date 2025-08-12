# Insert an element at 2nd index
def insert_at_index(given_list, element):
    if given_list == [] or len(given_list) < 3:
        return "Please give atleast three elements in the list"
    else:
        given_list.insert(2, element)
        return given_list
