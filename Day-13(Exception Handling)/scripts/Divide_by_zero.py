# Division by Zero Handling
def safe_divide(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        return "Cannot divide by zero"