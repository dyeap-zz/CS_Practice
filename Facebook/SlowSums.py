'''
slow sums


add two numbers. and put it in the list

keep going until there is only one number

choose max two numbers and then add them?

you pay penalty to add them. you want to do that because when you add it compounds

3,2,1

3+2 = 5

3+2+1

5+5+1=11

v,x,y,z


sum = (z+y) + (z+y) + x + (z+y+x) + v

(z+y) * (n-1) + x + (n-2) + v + (n-3)

sort the numbers. add as you go down.

time - n log n

space is O(1)

1. sort.
2. add left two numbers. i = 1
3. keep compounding as you go down the list
        *(n-i)  i = 2

can probaly do with a math equation?
input: array
output: int

arr = [4, 2, 1, 3]
output = 26

'''
def slowsum(arr):
    arr.sort()
    n = len(arr)
    # add the left two numbers
    if n < 2:
        return 0
    i, j = 2, n-3
    res = (arr[-1] + arr[-2])*(n-1) # 7*3 + 2*2 + 3*1

    while j >= 0: # 0
        res += arr[j]*(n-i)
        # update
        j -= 1
        i += 1 # 3
    return res

# 1,2,3,4
def slowsum(arr):
    arr.sort()
    n = len(arr)
    if n < 2: return 0

    res = arr[-1] + arr[-2] # 7
    prev = res
    for i in range(n-3,-1,-1): # 1
        prev += arr[i] # 17
        res += prev   # 16
    return res


arr = [2,3,9,8,4]
print(slowsum(arr))


print(min([3,4,5]))

n = 5
arr = [6,2,4]
for l in range(1, n): # loop everything 1-n. Don't do the leftmost/rightmost end
    for i in range(0, n-1): # left side -> start with 0 and stop -2 from the right
        j = i + l # stopping condition left_start + left_end
        print('j = ',j)
        for k in range(i, j): # left most side to
            print("j = ",l)
            print("i = ", i)
            print("k = ", k,'\n')


'''
0 1 2 3 4
    i
    k
    l
'''
''' 
    for i in range(0, i < n-l):
       j = i+l
       for k in range(i,k<j):
           print('l = ',l)
           #print(i = )
           #dp[i][j] = max(dp[i][j], dp[i][k] + result[k] + dp[k+1][j]);
'''


