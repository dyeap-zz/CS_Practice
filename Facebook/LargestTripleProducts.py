'''
n = 5
arr = [1, 2, 3, 4, 5]
output = [-1, -1, 6, 24, 60]

make a heap and then have it always store 3 values

1. create heap
2. append to heap and generate product only on i == 2

python uses minheap. compare min heap and see if you can replace

var - max_prod, heap, res
use a for loop:  3x
    1. add to heapq
    2 update max_prod
    3. if thrid time update res
use a while loop: # catch less than 3
    1. see if you can replace min element - peek
    2. pop, push
    3. update max_prod
    4. update res

edge cases: array size less than 3


n = 5
arr = [1, 2, 3, 4, 5]
output = [-1, -1, 6, 24, 60]
'''
import heapq
def findmaxProduct(arr):
    res, max_prod, h, n, i = [], 1, [], len(arr), 0

    # i 0 to 2
    while i<3   : #0<2
        num = arr[i] # 1
        heapq.heappush(h,num) # [1,2,3]
        max_prod *= num # 6
        if i < 2:
            res.append(-1) # -1,-1,6,24
        else:
            res.append(max_prod)
        i += 1

    # large than 2
    while i<n: # 4 < 5
        print(max_prod)
        num = arr[i]
        #min_num = h[0]
        #print(h[0])
        if num > h[0]: #    5 > 2
            max_prod /= heapq.heappop(h) # 60
            heapq.heappush(h,num)  #[5,3,4]
            max_prod *= num
        res.append(max_prod)
        i += 1

    return res

'''
1. loop:
2.      always put onto heapq
3.      if less than 3 then 
4.      else pop 3 and the 3 back
'''
def findmaxProduct(arr):
    res, h = [], []
    for i,num in enumerate(arr):
        heapq.heappush(h,-num)
        if (i<2):
            res.append(-1)
        else:
            x,y,z = heapq.heappop(h), heapq.heappop(h), heapq.heappop(h)
            prod = -x*y*z
            heapq.heappush(h,x)
            heapq.heappush(h,y)
            heapq.heappush(h,z)
            res.append(prod)
    return res


arr = [1, 2, 3, 4, 5]
print(findmaxProduct(arr))