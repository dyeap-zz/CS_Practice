'''
Given an array of integers arr, write a function absSort(arr),
that sorts the array according to the absolute values of the numbers in arr.
If two numbers have the same absolute value, sort them according to sign,
where the negative numbers come before the positive numbers.

Examples:

input:  arr = [2, -7, -2, -2, 0]
output: [0, -2, -2, 2, -7]

a = 2, b = 7 ret -1 left is smaller
a = -7, b = 2 ret 1 right is smaller

a = -2, b = 2 ret -1 left is smaller
a = 2, b = -2 ret 1 right is smaller

a = 2, b = 2 or a = 0, b = 0 either can be used
'''
#custom comparator

def absSort(arr):
  def compare(a,b):
    if abs(a) < abs(b): return -1
    if abs(a) > abs(b): return 1
    if a < b: return -1
    if a > b: return 1
    return 0

  arr.sort(key = compare)
  return arr

arr = [2, -7, -2, -2, 0]
print(absSort(arr))