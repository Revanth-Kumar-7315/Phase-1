# Count how many times 5 appears
def count_five(given_list):
    if given_list == []:
        return "Please give atleast one element in the list"
    else:
        return f"There are {given_list.count(5)} fives in the list"
