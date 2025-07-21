from collections import deque

data = [1, 2, 3, 4, 5, 6]
window_size = 3
window = deque(maxlen=window_size)

print("Sliding window:")
for num in data:
    window.append(num)
    print(list(window))
