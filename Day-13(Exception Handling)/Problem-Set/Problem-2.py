# Password Validator
class WeakPasswordError(Exception):
    pass


def validate_password(password):
        if len(password) < 8:
            raise WeakPasswordError("Password must be at least 8 characters long.")
        if not (any(char.isdigit() for char in password)):
            raise WeakPasswordError("Password must contain at least one digit.")
        return "Password is Valid"
            
try:
    print(validate_password('Revanth_reddy'))
except WeakPasswordError as e:
    print(e)