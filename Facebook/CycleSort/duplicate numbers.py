'''
Problem Statement
We are given an unsorted array containing ‘n’ numbers taken from the range 1 to ‘n’.
The array has some duplicates, find all the duplicate numbers without using any extra space.

Example 1:

Input: [3, 4, 4, 5, 5]
        0, 1, 2, 3, 4
Output: [4, 5]

Example 2:

Input: [5, 4, 7, 2, 3, 5, 3]
Output: [3, 5]
'''

def find_dup(arr):
    for i in range(len(arr)):
        num = abs(arr[i])-1
        if arr[num] < 0:
            return num+1
        else:
            arr[num] *= -1

arr = [2, 1, 3, 3, 5, 4]
print(find_dup(arr))

def find_miss(arr):
    e_sum = 0
    i_sum = 0
    for i in range(len(arr)):
        i_sum += i + 1
        e_sum += arr[i]

    return i_sum - e_sum
arr = [8, 3, 5, 2, 4, 6, 0, 1]
       #1,2,3,4 = 10
print(find_miss(arr))




