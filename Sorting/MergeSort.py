# base case: if (len(nums) == 1): return nums



#[3,2,1,4]

def merge_sort(nums):
    if (len(nums) == 1):
        return nums
    mid = len(nums)//2
    left_nums = merge_sort(nums[0:mid])
    right_nums = merge_sort(nums[mid:len(nums)])
    return merge(left_nums,right_nums)

def merge(left_li,right_li):
    res = []
    left_index = 0
    right_index = 0
    while (left_index < len(left_li) and right_index < len(right_li)):
        if (left_li[left_index] < right_li[right_index]):
            res.append(left_li[left_index])
            left_index += 1
        else:
            res.append(right_li[right_index])
            right_index += 1

    print(left_li,left_index,left_li[left_index:])
    res = res + left_li[left_index:] + right_li[right_index:]

    return res
print(merge_sort([1,3,6,3,7,1,9]))