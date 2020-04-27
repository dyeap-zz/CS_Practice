import math
def heapify_up(nums,index):
    # find out if the appended node is on the odd or even side
    if (index%2):
        p_index = math.ceil(index/2) - 1
    # on left side
    else:
        p_index = math.floor(index/2) - 1
    if (index < 1 or p_index < 0):
        return
    parent = nums[p_index]
    child = nums[index]
    if (child < parent):
        nums[p_index], nums[index] = nums[index], nums[p_index]
    heapify_up(nums,p_index)
    return

def insert_heap(nums,val):
    nums.append(val)
    heapify_up(nums,len(nums)-1)
    return

nums =[]
insert_heap(nums,6)
insert_heap(nums,3)
insert_heap(nums,1)
insert_heap(nums,-1)
insert_heap(nums,0)
insert_heap(nums,-2)
print(nums)
