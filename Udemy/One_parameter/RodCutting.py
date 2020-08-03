'''
cut the rod into different lengths to get max profit


index is the length and element is the profit
if index is greater than rod length then we can't cut it

states
curr_rod_length - rod
current rod i -

return the max profit


if can't cut: 0
if rod length == 0 or can't cut: 0


rod = 1, profit = []
# use the length of profit figure out if you can cut
max_profit(rod, profit,i)

base case
if rod length is smaller: 0

recrusive case can cut the rod rod>len(profit)
max(proft[i] + solve(rod-i,i+1),solve(rod,i+1))
'''
#memoize



# idea: if you make cut you can make the same cut again don't increment i. if not cut
# then increment i
# this method must use dp table not array because of multiple states
def max_cut(rod,profit,i,dp):
    # base case
    if i > rod or i>len(profit) or rod <= 0: return 0

    # recursive case
    if dp[i][rod] > 0: return dp[i][rod]
    res = max(profit[i-1]+max_cut(rod-i,profit,i,dp),max_cut(rod,profit,i+1,dp))
    dp[i][rod] = res
    return res

rod = 8
profit = [1,5,8,9,10,14,17,20,24,30]
dp = [[-1 for _ in range(rod+1)]for _ in range(len(profit))]
print(max_cut(rod,profit,1,dp))
print(dp)

'''
rod = 3
profit = [1,5,8,9,10,14,17,20,24,30]
dp = [-1] * len(profit)
print(max_cut(rod,profit,1,dp))
'''
'''
#state is length l


#backtracking

Length = 2
# base case
if rod len is 0: 0
#recursive case
for lens

recurrence relation
maxP(i,P) = max(p[i]+maxP(L-i-1,P)) for i = 0,1,2...L-1
'''
#1,2,3,4
#1,5,8,9
def max_cut(rod_len, profit, dp):
    # base case
    if rod_len == 0:return 0
    # recursive case 1+ greater rod length
    if dp[rod_len] != -1: return dp[rod_len]
    res = float('-inf')
    for i in range(1,rod_len):
        res = max(res,profit[i] + max_cut(rod_len-i-1,profit,dp))
    dp[rod_len] = res
    return res

#rod = 2
#profit = [1,5,8,9,10,14,17,20,24,30]
dp = [-1] * len(profit)
print(max_cut(rod,profit,dp))
print(dp)

# conclusion
# you can repeat usage of rod
# rod length is same as knapsack problem


# difference between using take the house and not take the house
# bottom up solution

# use dp array

# change dp array equation

# base case?
'''
base case starts with 0
make 1 extra space for dp array


dp = len(profit) + 1
profit

res =
dp[i] = max(res,profit[i-1])


rod = 4
profit = [1,5,8,9,10,14,17,20,24,30]


len = 2
profit[1,2,3]
dp = [0]
1. base case 0

loop: rl for all 1-rod_len
loop: j all 1-rl+1
    res = max(res,profit[j-1] + dp[rl-j])
dp[i] = res


1. create dp array +1 all 0
2. base case
3. alg

'''
def max_cut_BP(rod,profit):
    # create dp array
    dp = [0] * (len(profit) + 1)

    for rl in range(1,rod+1):
        for j in range(1,rl+1):
            dp[rl] = max(dp[rl],profit[j-1] + dp[rl-j])
    print(dp)
    return max(dp)


def max_cut_BP(rod,profit):
    # create dp array
    #dp = [0] * (len(profit) + 1)
    dp = [0] * (rod+1)

    for rl in range(1,rod+1):
        for j in range(rl):
            dp[rl] = max(dp[rl],profit[j] + dp[rl-j-1])
    print(dp)
    return dp[rod]

#rod = 7
#profit = [1,5,8,9,10,14,17,20,24,30]
print(max_cut_BP(rod,profit))

'''
rod = 0
rod = 3
dp = [0,1,5,8]
dp[4-1] = 1+dp[3] = 
dp[4-2] = 5+dp[2] = 10
dp[4-3] = 8+dp[1] = 9
dp[4-4]

profit[rl] + dp[2-2]

dp[i] = max(res,profit[i-1] + dp[i])



loop all dp
dp of cut of no cut
    res = res,pro[i-1] + dp[rod_len-i]

'''



def max_cut_BP(rod,profit):
    # create dp array
    #dp = [0] * (len(profit) + 1)
    dp = [0] * (rod+1)
    decision = [-1] * (rod + 1)

    for rl in range(1,rod+1):

        for j in range(rl):
            cut = profit[j] + dp[rl-j-1]
            no_cut = dp[rl]
            dp[rl] = max(cut, no_cut)
            # if you made a cut logged as max then you cache yes
            if cut>no_cut:
                decision[rl] = j+1#rl-j-1

    print(dp)
    res = []
    i = len(decision)-1
    print("lol")
    print(decision)
    while i != 0:
        res.append(decision[i])
        i -= decision[i]
    #res.append(i+1)
    print(res)
    #print(decision)
    return dp[rod]

print("lol")
print(profit,rod)
max_cut_BP(rod,profit)
# to reconstruct solution we need to log what rod we previously picked
# or yes/no we made a cut
