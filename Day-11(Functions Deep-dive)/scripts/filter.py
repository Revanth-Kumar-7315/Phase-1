# Use filter() function to select prime numbers from a list.
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def filter_primes(numbers):
    return filter(is_prime, numbers)


# Example usage:
if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    primes = list(filter_primes(numbers))
    print("Prime numbers:", primes)
# --- IGNORE ---
