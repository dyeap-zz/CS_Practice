'''
Given an array of integers and an integer k,
you need to find the total number of continuous
subarrays whose sum equals to k.

Input:nums = [1,1,1], k = 2
Output: 2
'''

Recursion Structure


func(nums,k,index)
# base case
if index > len(nums): return 0
# recursive case start at a different starting point

sum = 0
res = 0
for i in range(index,len(nums)):
    sum += num[i]
    # this is the key to checking different end points
    if sum == k:
        res += 1

return res + recurse(arr,k,index+1) // go to next index and find annswer


extra work?