'''
recurrence relation

bin_coeff(n,k) = bin_coeff(n-1,k-1) + bin_coeff(n-1,k)

if n == k: 1
if k = 0: 1
'''
n = 10
k = 5
def bin_coeff(n,k):
    # base case
    if k > n: return 0
    if n == k: return 1
    if k == 0: return 1
    # recursive case
    return bin_coeff(n-1,k-1) + bin_coeff(n-1,k)

print(bin_coeff(n,k))

def bin_coeff(n,k,cache):
    # base case
    if k > n: return 0
    if n == k or k == 0:
        cache[(n,k)] = 1
        return 1
    # recursive case
    if (n,k) in cache: return cache[(n,k)]
    cache[(n,k)] = bin_coeff(n-1,k-1,cache) + bin_coeff(n-1,k,cache)
    return cache[(n,k)]

print(bin_coeff(n,k,{}))
'''
# bottom up
bc(7,5) = bc(6,4) + bc(6,5)
bc(6,4) = bc(5,3)

1. init base cases
2. how to iterate through

bc(1,2) = bc(0,1) + bc(0,2)
bc(2,1) = bc(1,0) + bc(1,1)

(n,k)
  0 1 2 3
0 1 0 0 0
1 1 1 0 0
2 1 2
3 1

1. init dp table of all 0
2. fill in all col of k
3. if k > n: 0
'''
def bin_coeff_bot(n,k):
    if k > n: return 0
    dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
    # set up base case
    for row in range(n+1):
        dp[row][0] = 1
    # recurse through
    for row in range(n+1):
        for col in range(k+1):
            # when k == n
            if row == col:
                dp[row][col] = 1
                break
            dp[row][col] = dp[row-1][col-1] +  dp[row-1][col]
    return dp[-1][-1]

print(bin_coeff_bot(n,k))


