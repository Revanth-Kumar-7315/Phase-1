# Raise a ValueError for Negative Numbers
def check_positive(num):
    try:
        if num < 0:
            raise ValueError("Negative number not allowed")
        return 'Valid!'
    except ValueError as e:
        print(e)