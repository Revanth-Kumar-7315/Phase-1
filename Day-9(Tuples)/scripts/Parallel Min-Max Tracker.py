# Parallel Min-Max Tracker
# temps_day = [28, 35, 30, 33]
# temps_night = [22, 25, 21, 24]
def parallel_min_max_tracker(temps_day, temps_night):
    """
    Finds the minimum and maximum temperatures from two lists of temperatures.

    :param temps_day: List of daytime temperatures.
    :param temps_night: List of nighttime temperatures.
    :return: Tuple containing the minimum and maximum temperatures.
    """
    min_temp = min(min(temps_day), min(temps_night))
    max_temp = max(max(temps_day), max(temps_night))
    return (min_temp, max_temp)
