# A function that returns the maximum of three numbers
def max_of_three(num_1, num_2, num_3):
    if num_1 > num_2 and num_1 > num_3:
        return f"{num_1} is the maximum among the three numbers"
    elif num_2 > num_3:
        return f"{num_2} is the maximum among the three numbers"
    else:
        return f"{num_3} is the maximum among the three numbers"
