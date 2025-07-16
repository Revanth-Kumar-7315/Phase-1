# Create a dictionary from 2 lists
def create_dict_from_lists(list_1, list_2):
    dictionary = {}
    if len(list_1) != len(list_2):
        return "Not possible"
    else:
        return dict(zip(list_1, list_2))
