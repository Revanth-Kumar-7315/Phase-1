# Count how many numbers are greater than the average
def count_greater_than_avg(lst):
    average = sum(lst) / len(lst)
    count_of_greater_than_avg = 0
    for i in lst:
        if i > average:
            count_of_greater_than_avg += 1
    return count_of_greater_than_avg
