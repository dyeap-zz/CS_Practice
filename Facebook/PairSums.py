'''
same as pair if two numbers

dict

complment of number and num of occurences

1. loop:
    if num in dict: occ+1
    store complement on number in dict

dict = {5:1,4:1,3:1}

'''
def pair_sums(arr,k): # res = 2
    d, res = {}, 0 # d = {5:1,1:1,3:2}
    for num in arr: # 1
        if num in d:
            res += d[num]
        # must always update
        if k-num not in d:
            d[k-num] = 1
        else:
            d[k-num] += 1
    return res


k = 6
arr = [1, 5, 3, 3, 3]
print(pair_sums(arr,k))