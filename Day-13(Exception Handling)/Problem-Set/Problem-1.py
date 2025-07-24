# Safe Integer Input
def get_safe_integer():
    while True:
        try:
            user_input = int(input("🔢 Enter a valid integer: "))
            print(f"✅ You entered: {user_input}")
            break
        except ValueError:
            print("❌ Invalid input. Please enter a numeric integer.")
get_safe_integer()