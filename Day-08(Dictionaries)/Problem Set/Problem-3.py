# Return dict of even numbers and their squares
def even_squares(List):
    return {i: i**2 for i in List if i % 2 == 0}
