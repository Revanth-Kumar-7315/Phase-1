# Filter Even-Squared Pairs with Tuples
def filter_even_squared_pairs(pairs):
    """
    Filters out pairs where the first element is even and returns a list of tuples
    with the first element squared.

    :param pairs: List of tuples, where each tuple contains two integers.
    :return: List of tuples with the first element squared if it is even.
    """
    return [(x**2, y) for x, y in pairs if x % 2 == 0]
