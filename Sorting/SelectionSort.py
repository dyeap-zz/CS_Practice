# iterate i through 0,len(nums)
# iterate through i,len(nums)
#   if min
#   swap
#   reset min

# [3,2,1]

def sel_sort(nums):
    for start in range(0,len(nums)):
        min_index = start
        for j in range(start,len(nums)):
            if (nums[j] < nums[min_index]):
                min_index = j
        nums[start], nums[min_index] = nums[min_index], nums[start]
    return nums

nums = [7,3,9,4,10]
print(sel_sort(nums))