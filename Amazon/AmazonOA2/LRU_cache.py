'''
set() - what is in cache.to
look
queue() - [old->newest]
loop
memory:
1.
cache
hit -
remove
from queue.append to

end
of
queue
2.
cache
miss -
if cache is full -> remove oldest -> popleft
append
new
element
'''

from collections import deque
def lruCacheMisses(num: int, pages: list, maxCacheSize: int) -> int:                    
    q = deque([])
    #q_size = 0
    s = set()
    res = 0

    for page in pages:
        #print("page = %d"%page)
        #print(q)
        #print("cache")
        #print("\n")

        # cache hit
        if page in s:
            q.remove(page)
            q.append(page)
        else:
            res += 1
            if len(q) == maxCacheSize:
                oldest = q.popleft()
                s.remove(oldest)
            q.append(page)
            s.add(page)

    return res