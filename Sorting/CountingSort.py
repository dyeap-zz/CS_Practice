'''
1. find max number and create list of that size
2. for each number store occ
3. DP - for each number take prev and add to curr occ 1-len
4. create list of that size and decrement to put into last index for each num in list
'''
arr = [3,6,2,8,9,1,3,4,5,4,3,3,4,6,7,100]

max_num = max(arr)

occ = [0] * (max_num+1)
for num in arr:
    occ[num] += 1

for i in range(1,len(occ)):
    occ[i] = occ[i-1] + occ[i]

sort_arr = [None] * len(arr)
for num in arr:
    last_index = occ[num]-1
    sort_arr[last_index] = num
    occ[num] -=1

print(sort_arr)

#run time O(n+k)
# n is numbers in list, k is num occ in list
# space O(k) k is max number
# Basically linear for everything unless range is large



