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


#PYTHON DOES NOT HAVE A CMP =, IT USES KEY =
'''
def absSort(arr):
  def cmp(a,b):
    if abs(a) < abs(b): return -1
    if abs(a) > abs(b): return 1
    if a < b: return -1
    if a > b: return 1
    return 0

  arr.sort(key = cmp)
  #a = sorted(arr,key = cmp)
  return arr

arr = [2, -7, -2, -2, 0]
print(absSort(arr))

# custom comparator sort
'''

arr = [[4,2],[1,2],[0,3]]

arr.sort(key=lambda x: x[0])
print(arr)


li = [30,3,34]
class cmp(str):
    def __lt__(x, y):
        return x+y > y+x

li.sort(key = cmp)
s = [str(num) for num in li]
res = "".join(s)
print(res)