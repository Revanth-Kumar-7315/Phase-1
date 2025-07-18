# Index of the Max Value by using Tuples
def index_of_max_value(tup):
    if not tup:
        return None  # Return None if the tuple is empty

    max_value = max(tup)  # Find the maximum value in the tuple
    max_index = tup.index(max_value)  # Get the index of the maximum value
    return max_index  # Return the index of the maximum value
