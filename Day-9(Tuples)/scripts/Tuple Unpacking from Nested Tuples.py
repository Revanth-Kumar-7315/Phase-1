# Tuple Unpacking from Nested Tuples
# people = [('Ram', 25), ('Shyam', 32), ('Geeta', 29)]
def unpack_nested_tuples(nested_tuples):
    """
    Unpacks a list of nested tuples into a list of dictionaries.

    :param nested_tuples: List of tuples, where each tuple contains a name and an age.
    :return: List of dictionaries with 'name' and 'age' keys.
    """
    return [{"name": name, "age": age} for name, age in nested_tuples]
