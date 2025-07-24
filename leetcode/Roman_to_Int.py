def romanToInt(s):
    decipher = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500,'M' : 1000}
    prev_value = 0
    result = 0
    for i in s[::-1]:
        present_value = decipher[i]
        if present_value >= prev_value:
            result += present_value
            prev_value = present_value
        else:
            result -= present_value
            prev_value = present_value
    return result