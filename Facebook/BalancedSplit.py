# arr = [1, 5, 7, 1]
'''
Must try every combination

brute force method:
loop i:
    recursion try every combination. see if you can get that sum


sort all the numbers

try to find a balanced split

add up all the numbers

move pointer until unique number
loop: while i
    if prev = curr num
        left += num[i]
        right -= num[i]
        c += 1
      else:
          if left = right: True

          p = c


1,1,2,3
    p
      c

'''


def balanced_split(arr):
    if len(arr) <= 1: return False

    # more than one number
    arr.sort()

    p,c,l,r = 0, 0, 0, 0

    l,r = 0, sum(arr) # l = 7, 7
    while c < len(arr): # 0
        if arr[p] == arr[c]: # 1 == 1
            l += arr[c] 
            r -= arr[c]
            c += 1
        else:
            if l == r:
                return True
            p = c
    return False


#arr = [3, 6, 3, 4, 4]
#print(balanced_split(arr))


# quickselect
#https://leetcode.com/discuss/interview-question/718692/facebook-training-balanced-split

'''
quicksort on rightmost element
as you swap add to lsum and subtract from rsum

if lsum > r_sum: pick on leftside
else
pick another pivot on right side

must pick something not equal to previous pivot

1. parititon: pivot_index,l,r

2.  n= quickselect
    0. sum everything
    1. create two list:low and high
    2. if <= add to lsum
    3. else high

    3. low, high, lsum

    if choose low: new_v = low
    else choose high: update lsum and new_v = high
'''
def partition(arr,lsum,piv,total):
    low,high = [],[]
    csum = lsum
    for num in arr:
        if num <= piv:
            csum += num
            if num < piv:
                low.append(num)
        else:
            high.append(num)
    # update arr
    if (2*csum <= total):
        arr = high
        lsum = csum
    else:
        arr = low
    return lsum,arr

def balanced_split(arr):
    if len(arr) <= 1: return False

    total = sum(arr)
    lsum = 0

    while arr:
        piv = arr[-1] 
        lsum,arr = partition(arr,lsum,piv,total) # 2,[5,7]
        if (2 * lsum == total): return True
    return False

arr = [20,2]
print(balanced_split(arr))

