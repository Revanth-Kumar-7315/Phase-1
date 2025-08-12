# Rotate list right by 1 position
def rotate_right(lst):
    if not lst:
        return lst
    else:
        return [lst[-1]] + lst[:-1]
