'''
Input: [3, 1, 5, 4, 2]
Output: [1, 2, 3, 4, 5]



sort in place. number are 1-n

could just go thourhg and rewrite numbers

only swapping?

[1,2,3,4,5]

while arr:
    if not then:
        swap
    if index = num-1:
        move i up
        continue
'''
def cycle_sort(arr):
    if len(arr) < 1:
        return []

    i, n = 0, len(arr)
    while i < n: # 0 < 5
        num = arr[i] # 2
        if i == num-1: #0 == 1
            i += 1
            continue
        else:
            arr[i], arr[num-1] = arr[num-1], arr[i]

    return arr

arr = [2, 6, 4, 3, 1, 5]
print(cycle_sort(arr))


