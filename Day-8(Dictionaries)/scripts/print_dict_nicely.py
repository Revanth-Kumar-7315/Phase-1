# Loop over a dictionary and format output
def print_dict_nicely(dictionary):
    for key, value in dictionary.items():
        print(f"{key}: {value}")
    return None


# Example usage:
# my_dict = {'a': 1, 'b': 2, 'c': 3}
# print_dict_nicely(my_dict)
# This will print:
# a: 1
# b: 2
# c: 3
# Note: This function does not return anything, it just prints the formatted output.
# It can be used to display dictionaries in a readable format.
