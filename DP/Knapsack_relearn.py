'''
#knapsack

given a specific weight and a set of items with weight and val how to pick which
items to put in the bag to get max value out of bag

states
w - weight of bag
i - index of item considered

function returns the max profit for a weight and index i

state transitions
what are choices are every recursive step - either put item in bag or not

W = weight, i=last_index

base case
if weight is 0 or index is -1: 0

recursive case - more items to consider
res = 0
for items in bag
    if can fit
        res = max(res,solve(W-weight[i],i-1))


skip item - solve(W,i-1)
put item in bag - val[i] + solve(W-weight[i],i-1))
recurrence relation
solve(W,i) = max(solve(W,i-1),val[i] + solve(W-weight[i],i-1)))       W = 0,...W, i = 0,1,2,3,...n
'''



# recursive solution
def max_profit(W,i,val,weight):
    # base case
    if W == 0 or i == -1: return 0

    # recursive case
    res = 0
    for idx in range(i,-1,-1):
        # can fit in the bag
        if weight[idx] <= W:
            res = max(res,val[idx]+max_profit(W-weight[idx],idx-1,val,weight))

    return res

#  DP
def max_profit_DP(W, i, val, weight, dp):
    # base case
    if W == 0 or i == -1: return 0

    # recursive case
    if dp[W][i] != 0: return dp[W][i]
    res = 0
    for idx in range(i, -1, -1):
        # can fit in the bag
        if weight[idx] <= W:
            res = max(res, val[idx] + max_profit_DP(W - weight[idx], idx - 1, val, weight, dp))
    dp[W][i] = res
    return res

'''
W = 50
weight = [1,10,20,30]
val = [1000,60,100,120]
'''
weight = [3, 7, 10, 6]
val = [4, 14, 10, 5]
W = 20
dp = [[0 for _ in range(len(val))] for _ in range(W+1)]
print(max_profit(W,len(weight)-1,val,weight))
print(max_profit_DP(W,len(weight)-1,val,weight,dp))

'''
bottom up

1. size of dp table? +1
2. initialize base case?
3. alg?

base case
set all init values to -1

do you need extra slots for base case? Yes

dp[Weights+1][num_items+1]


bottom up equation
solve(W,i) = max(solve(W,i-1),val[i] + solve(W-weight[i],i-1)))
include = val[i] + dp[W-weight[i]][i-1]
exclude = dp[W][i-1]
dp[W][i] = max(include,exclude)


base case
for all W == 0, dp = 0
for all i == 0, dp = 0

W = 4
weight = [9,4,1,3]
val = [5,2,7,4]
output = 11

dp
W = 2, i = 3
(W,i)
  0 1 2 3 4
0 0 0 0 0 0
1 0 0 0 7 7
2 0 0 0 7 7
3 0 0 0 7 7
4 0 0 2 7 11
'''
def max_profit_BP(weight,val):
    # dp table
    dp = [[-1 for _ in range(len(val)+1)] for _ in range(W + 1)]

    # base case
    for r in range(len(weight)+1):
        dp[r][0] = 0

    for c in range(len(weight)+1):
        dp[0][c] = 0

    # alg
    for i in range(1,len(val)+1):
        for w in range(1,W+1):
            #print(w)
            if weight[i-1] <= w:
                dp[w][i] = max(val[i-1]+dp[w-weight[i-1]][i-1],dp[w][i-1])
            else:
                dp[w][i] = dp[w][i-1]
    print(dp)
    return dp[-1][-1]

#W = 4
#weight = [9,4,1,3]
#val = [5,2,7,4]
print(max_profit_BP(weight, val))