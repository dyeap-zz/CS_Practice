'''
Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.





state
i - from i to end of array
returns length of lis from i to end of array

state transition
n = len(arr)
start with i = n-1

recurrence relation
lis(i) = max(lis(idx))    idx = i,i+1,i+2,...n

at every index we have two choices. put the number into lis or don't put it in


base case
if i is past last num: ret 0


recursive case
if arr[idx] > arr[i]: 1+lis(idx+1)
else: go to next index

recursive solution

[1,2,3]
   idx  i
   '''
def lis(nums, i):
    # base case
    if i == 0: return 1

    # recrusive case
    res = 1
    for j in range(i,-1,-1):
        for idx in range(j-1,-1,-1):
            if nums[idx] < nums[j]:
                res = max(res,1+lis(nums,idx))

    return res

nums = [100,101,3,4]
print(lis(nums,len(nums)-1))

