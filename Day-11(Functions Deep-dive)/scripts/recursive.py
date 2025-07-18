# Recursive function to compute factorial and Fibonacci.
def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)


def fibonacci(n):
    return n if n <= 1 else fibonacci(n - 1) + fibonacci(n - 2)


def main():
    print("Factorial of 5:", factorial(5))
    print("Fibonacci of 5:", fibonacci(5))


if __name__ == "__main__":
    main()
