# Use assert to Validate Input
def validate_age(age):
    try:
        assert age >= 0, "Age must be positive"
    except AssertionError as e:
        return str(e)
    else:
        return 'Valid'