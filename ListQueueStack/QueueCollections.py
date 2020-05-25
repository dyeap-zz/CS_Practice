import collections
from copy import copy
de = collections.deque([1,2,3])
ce = copy(de)
de.appendleft(0)
de.append(5)
print(de.popleft())
print(de.pop())
print(de.remove(2))

print(ce)
print(de)

