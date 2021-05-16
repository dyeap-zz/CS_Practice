'''
detect unique characters

start L/R beginning
move R pointer up until k+1 unique char.
    longest = l+R-1

move L pointer until k unique char


var-
num_unique_char
dictionary to keep track of num off occ

0 to 1 num_unique_char + 1
1 to 0 num_unique_char - 1

while r<len

    update r

    if num_uni == k:
        1. store res
        while move left
        2. move left until d[num] ==0

   update r
'''
def longest_unique(arr,k):
    res = -1
    l, r, u = 0 , 0, 0
    d = {}


    # move r
    while r < len(arr):
        num = arr[r]
        if num not in d or d[num] == 0:
            u += 1
            d[num] = 1
        else:
            d[num] += 1

        # left
        if u == k+1:
            #print(l,r)
            res = max(res,r-l)
            while True:
                #print(l)
                l_num = arr[l]
                d[l_num] -= 1
                l += 1
                if d[arr[l-1]] == 0:
                    u -= 1
                    break
        r += 1

    if u == k:
        res = max(res,r-l)
    return res

arr = "aabbcc"
k = 3
print(longest_unique(arr,k))