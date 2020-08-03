'''
1. get a random pivot
2. move all numbers to left and right
3.

4,3,6,5
      p
8,4,3,5,6
      p
qs(arr,l,r)
if num goes on left: keep going
if goes on right:
    temp = larger num
    num below pivot goes to num position
    pivot goes one down
    larger num goes to pivot location

qs(left of pivot)
qs(right of pivot)

1. index of pivot = qs(full array)
2. qs(left of pivot)
3. qs(right of pivot)
return

1,2,3,7,5
      l
        p
'''
1. pointer for i - the first index of number larger than pivot
2. if num is less than pivot then you swap i and j
3. at the end swap pivot with i and return i
def qs(arr,l,r):
    #if l == r: return l
    x = arr[r]
    i = l
    for j in range(l, r):

        if arr[j] <= x:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[i], arr[r] = arr[r], arr[i]
    return i

'''
    p = r
    while l != p:
        left_num = nums[l]
        pivot_num = nums[p]
        if left_num < pivot_num: l += 1
        elif left_num >= pivot_num:
            temp = left_num
            nums[l] = nums[p-1]
            nums[p-1] = nums[p]
            nums[p] = temp
            p -= 1
    return p
    '''

def quicksort(nums,l,r):
    if l >= r: return nums
    #if len(nums) <= 1: return nums
    p = qs(nums,l,r)
    quicksort(nums,0,p-1)
    quicksort(nums,p+1,r)
    return nums


'''

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
'''
nums = [6,3,6,0,1,4,6,3]
print(quicksort(nums,0,len(nums)-1))

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