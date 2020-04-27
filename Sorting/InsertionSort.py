# iterate start 0,len(nums)
#   left = nums[start]
#  iterate index (start+1,0,-1)
#   if right < left
#       swap

# [2,1,3,0]

def ins_sort(nums):
    for left_ind in range(0,len(nums)-1):
        if (nums[left_ind] < nums[left_ind + 1]):
            continue
        for right_ind in range(left_ind + 1, 0, -1):
            left = nums[right_ind-1]
            right = nums[right_ind]
            if (right < left):
                nums[right_ind], nums[right_ind-1] = nums[right_ind-1], nums[right_ind]

    return nums

nums = [4,5,2,6,8,1]
print(ins_sort(nums))