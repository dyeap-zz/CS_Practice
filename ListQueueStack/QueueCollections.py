import collections

de = collections.deque([1,2,3])
de.appendleft(0)
de.append(5)
print(de.popleft())
print(de.pop())
print(de.remove(2))


print(de)

