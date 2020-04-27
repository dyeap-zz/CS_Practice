# two pointers
# for i thru len(nums)
# iterate j 0 thru end - i
#   prev_num = nums[j]
#   curr_num = nums[j+1]
#   if (prev_num > curr_num):
#       #swap()
#

# nums = [3,2,1]

def bubble_sort(nums):
    for i in range(0,len(nums)-1):
        for j in range(0,len(nums)-1):
            prev_num = nums[j]
            curr_num = nums[j+1]
            if (prev_num > curr_num):
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums

nums = [4,6,8,3,8,2]
print(bubble_sort(nums))


