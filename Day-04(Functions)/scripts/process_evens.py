# A function that returns sum + count of even numbers in a list
def process_evens(a):
    count = len([i for i in a if i % 2 == 0])
    total = sum([i for i in a if i % 2 == 0])
    return f"In the list {a} there are {count} even numbers and their sum is {total}"
