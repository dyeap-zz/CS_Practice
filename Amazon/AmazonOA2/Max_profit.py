# https://aonecode.com/maximize-profit
'''
1. cache of 100,001 -> start with 0
2. loop through input and +1 for occ
3. loop and if you add num of occ
4. subtract out excess

[4,3]
3+7
'''
def max_profit(arr,K):
    cache = [0 for _ in range(100001)]

    # fill cache
    for price in arr:
        cache[price] += 1

    res = 0
    mult = 0
    print(cache)
    num_items = 0
    for price in range(100000,-1,-1):
        occ = cache[price]

        # must add

        mult+=occ
        num_items += mult
        res += mult*price
        if num_items > 0:
            print("num_items=%d"%(num_items))
            print("res=%d" % (res))
        if num_items >= K:
            excess = K - num_items
            print(res)
            print("excess=%d"%excess)
            print("price=%d" % price)
            res += price*excess
            break
    return res

arr = [3,5,7,10,6]
K = 20
print(max_profit(arr,K))









