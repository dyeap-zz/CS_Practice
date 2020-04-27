# This method uses O(n) space. To use log n must pass everything by reference
# list slicing does not pass by reference. It makes a whole new list and passes it in

def qs(nums,pivot):
    left = 0
    while(pivot != left and pivot > left):
        print(nums,pivot,left)
        if (nums[left] > nums[pivot]):
            temp = nums[pivot]
            nums[pivot] = nums[left]
            nums[left] = nums[pivot - 1]
            nums[pivot - 1] = temp
            pivot -= 1
        else:
            left += 1
    print(nums)
    print("")
    return nums,pivot


def quicksort(nums):
    if (len(nums)< 2):
        return nums
    pivot = len(nums) - 1
    nums,pivot = qs(nums,pivot)
    print(pivot)
    left_qs = quicksort(nums[0:pivot])
    left_qs.append(nums[pivot])
    right_qs = quicksort(nums[pivot + 1:])
    return left_qs + right_qs

nums = [6,3,6,0,1,4,6,3]
print(quicksort(nums))

def test2(num):
    num = 3.4
num = 12.3
test2(num)
print(num)

def test(nums):
    nums[0] = -1
    #print(map(id,nums))
nums2 = nums[:]

test(nums2)
print(nums)
print(nums2)
#test(nums[0])
#print(nums)