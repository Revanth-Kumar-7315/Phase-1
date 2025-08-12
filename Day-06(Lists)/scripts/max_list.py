# Find max number using loop
def max_list(given_list):
    current_max = 0
    for i in given_list:
        if i > current_max:
            current_max = i
    return current_max
