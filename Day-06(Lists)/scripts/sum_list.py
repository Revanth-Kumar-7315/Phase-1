# Sum all numbers in list using loop
def sum_list(given_list):
    num_list = []
    for i in given_list:
        if type(i) == int:
            num_list.append(i)
    return sum(num_list)
