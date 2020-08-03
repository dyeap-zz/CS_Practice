'''
# find the minimum number of jumps to get to the end of list

input: given a list where each index stands for cost of landing on the space
assume that the list is positive numbers or 0
if negative you want to be able to jump backwards
[1,0,100,0]

solution where you always choose smallest and you don't get min coin'


[1,2  100,0   0]


if X is less than 1 then you can never get to the end

if X > len of list you it only cost 1 jump

if list is empty: 1 jump

1. states

index you jumped to - i

return the min cost to get to a particular index i

2. state transition

solve(cost,jump,i)
# base case
if X is greater than # of cost: cost[-1]

# recursive case can't make it to the end in one jump
for idx all i to (i+X):
    res = min(res,solve(idx))

recurrence relation:

[1,2,1]

must try every possible jump within range X going right

sol(i) = cost[i] + min(sol(idx))   ; idx = 1,2,...X, i  = 0,1,2,...len(cost)

start with i = 0
'''


'''
# bottom up solution

sol(i) = cost[i] + min(sol(idx))   ; idx = 1,2,...X, i  = 0,1,2,...len(cost)
every time this index is + jump


# base case we start at the end
dp is same length as cost

#dp[-1] = cost[-1]

    for end-end-jump
        dp[i] = min(dp[i],cost[i] + dp[j])

bottom up equation
dp[i] = cost[i] + min(dp[j])   ; idx = 1,2,...X, i  = 0,1,2,...len(cost)

do we need to do the first cost?

cost = [0,1,3,100,0,0] jump = 2
output = 2, 0,2,4,5
dp = [0,0,0,101,3,3]
index = [-1,-1,0,1,2,4]

1. outer for index in cost jump

cost = [0, 1, 3, 100, 0, 0]
jump = 2

dp = [,0,0]
index = [,]


dp = [0,1,2,101,2,0]
min_jump = [0,0,0,1,5,4]


cost = [1,2,100,2,1,0] jump = 2
dp = [1,2,101,3,1]
min_jump = [0,0,0,3,4]

1,3,5

1. len cost - float('inf') init
2. outer - start at jump + 1 to cost
3. inner - start at 0 to cost
'''

def min_cost_BP(cost,jump):
    if len(cost) == 0: return 0
    if jump >= len(cost): return cost[-1]
    # init dp array
    dp = [float('inf')] * len(cost)
    prev_jump = [-1] * len(cost)

    # base case
    for i in range(jump):
        dp[i] = cost[i]

    # alg
    for i in range(jump,len(cost)):
        for j in range(i-jump,i+1):
            curr_cost = cost[i] + dp[j]
            prev_cost = dp[i]
            if curr_cost < prev_cost:
                prev_jump[i] = j
            dp[i] = min(dp[i],cost[i] + dp[j])
    print(dp)

    i = len(prev_jump) - 1
    res = []
    print(prev_jump)
    while i > -1:
        res.append(i)
        if prev_jump[i] == -1: break
        i = prev_jump[i]
    print(res)
    return dp[-1]

cost = [4,2,5,1,2,100,0,0]
jump = 2
print(min_cost_BP(cost,jump))

'''
cost = [1,2,101,2,0]
dp = [1,2,102,4,4]
prev_jump = [-1,-1,0 ,1,4]

1. states
i - current index
cost function return min number of coins required to get to i

2. state transitions
start with i = last index
min_coins(cost,i,X)
# base case
if i is less than 0: cost = 0
# recursive case i is greater than 0
for idx : (i,i-X) 
    res = max(res,min_coins(idx))
return res
recurrence relation

min_cost(i) = cost[i] + min_cost(j,j-1,...j-X)
'''
def min_coins(cost,X,i):
    # base case
    if i < 0: return 0
    # recursive case
    res = float('inf')
    for idx in range(i-1,i-X-1,-1):
        res = min(res,cost[i] + min_coins(cost,X,idx))
    return res

print(min_coins(cost,jump,len(cost)-1))


def min_coins(cost,X,i,dp):
    # base case
    if i == 0: return 0
    # recursive case
    res = float('inf')
    end = min(X,i)+1
    for j in range(1,end):
        res = min(res,cost[i] + min_coins(cost,X,i-j,dp))
    dp[i] = res
    return res
dp = [-1] * len(cost)
print(min_coins(cost,jump,len(cost)-1,dp))
print(dp)

'''
def min_cost_dp(cost,X):
    N = len(cost)
    dp = [float('inf')] * N
    dp[0] = 0
    for i in range(0,N):
        for j in range(1,min(X,i)+1):
            dp[i] = min(dp[i],dp[i-j] + cost[i])
    return dp[N-1]

print('yes')
print(min_cost_dp(cost,jump))
'''