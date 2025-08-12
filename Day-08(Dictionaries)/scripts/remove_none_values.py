# Remove keys with None as value
def remove_none_values(dictionary):
    return {k: v for k, v in dictionary.items() if v is not None}
