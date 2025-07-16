# Invert a dictionary (swap keys and values)
def invert_dict(Dict):
    Dict_new = {}
    for key, value in Dict.items():
        Dict_new[value] = key
    return Dict_new
