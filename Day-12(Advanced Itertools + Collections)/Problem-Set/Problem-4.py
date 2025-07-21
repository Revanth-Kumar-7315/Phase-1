# Rolling Average using deque
from collections import deque

data = [1, 2, 3, 4, 5]
dq = deque(maxlen=3)
result = []

for i in data:
    dq.append(i)
    result.append(sum(dq) / len(dq))

print(result)
