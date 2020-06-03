# how to copy deque
from collections import deque
queue = deque([4,2,7,1])
layer = deque(queue)
queue = deque()

print(layer)
print(queue)