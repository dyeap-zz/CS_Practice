'''
loop for x times
1. pop x elements or until queue is empty ->  store max value and index
2. add to res the index
3. decrement by 1, min(0,num-1). if max == index. then don't add

use two queue.
'''
from collections import deque
def queue_removal(n,arr,x):
    q1,q2 = deque(), deque()
    res = []
    for i,num in enumerate(arr):
        q1.append([num,i+1])
    print(q1)
    for _ in range(x):
        max_val = -1
        sub_res = []
        # step 1
        for _ in range(x): #q1 = [5:6]
            if len(q1) == 0: break
            o = q1.popleft()
            num,j = o[0], o[1]
            if num > max_val: #3>2
                sub_res = o #[4:5]
                max_val = num
            q2.append(o)
        # step 2
        res.append(sub_res[1])

        # step 3 put everything back into q1
        while q2: #[1:1,2:2,2:3,3:4,4:5]
            o = q2.popleft()
            # remove largest num
            if sub_res == o:
                continue
            # append num
            num,_ = o[0],o[1]
            if num > 0:
                o[0] -= 1
            q1.append(o)
    return res



n = 13
arr= [2, 4, 2, 4, 3, 1, 2, 2, 3, 4, 3, 4, 4]
x = 4
print(queue_removal(n,arr,x))