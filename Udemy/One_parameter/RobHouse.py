'''
A robber can't rob the adj house. Find the max sum in the robber can get.
EX: S = [20,25,30,15,10]

states
house, index(i) -robbed

cost function solve(i,profit)
max profit at each index.
return the max profit at a particular house

choice - choose current house or prev house
state transitions
# base case
if no house: 0
if one house: return house
# recursive case 2+ houses
current = house[i] + solve(i-2)
!current = solve(i-1)
max(rob_current,don't rob_current)
'''

#i = 0

#[10,1,2]
#i = len(profit) - 1

#cache = [10,12]
def max_profit(profit,i,cache):
    # base case
    if i < 0 or len(profit) == 0: return 0
    # recursive case
    if i in cache: return cache[i]
    rob = profit[i] + max_profit(profit,i-2,cache)
    no_rob = max_profit(profit,i-1,cache)
    cache[i] = max(rob,no_rob)
    return cache[i]
'''
# bottom up approach
1. convert the recurrence relation

dp array = len(profit) + 1

0 poisiton will be the base case

init all dp values to 0

for 1-n:
    perform dp recurrenece


rob = house[i-2] + dp[i-2]
not_rob = dp[i-1]
dp[i] = max(rob,not_rob)

S = [20,25,30,15,10]

dp = [0,0,20,25,50,50,60]

'''
def max_profit_bot_up(profit):
    if len(profit) == 0: return 0

    dp = [0] *  (len(profit) + 2)

    for i in range(2,len(dp)):
        rob = profit[i-2] + dp[i-2] # 10 + 50
        not_rob = dp[i-1]
        dp[i] = max(rob,not_rob)

    return dp[-1]

profit = [10,3,2,10,2,4]
cache = [-1] * len(profit)
print(max_profit(profit,len(profit)-1,cache))
print(max_profit_bot_up(profit))

'''
which houses were robbed?

cache that logs which house was previously robbed

ex: [-1,10,5,20,100,4]
go until you reach the end or a -1
[-1,-1,-1,1,1,1,1,4]

var
res

house_robbed
loop: backward until -1
    prev != curr -> add to res
    
as you go bottom up you log which house had the max rob - house or dp[not_rob]

you log the prev house robbed to get there 

'''
#[10,20,30,1,50]
#[-1,-1,0,1,2,2,4]
#go backward put only take if house difference if by -2
def max_profit_bot_up_dec(profit):
    if len(profit) == 0: return 0

    dp = [0] *  (len(profit) + 2)
    decision = [-1] * (len(profit) + 2)
    dec = [False] * (len(profit) + 2)

    for i in range(2,len(dp)):
        rob = profit[i-2] + dp[i-2] # 10 + 50
        not_rob = dp[i-1]
        dp[i] = max(rob,not_rob)
        if rob > not_rob:
            decision[i] = i-2
            dec[i] = True
        else:
            decision[i] = decision[i-1]
            dec[i] = False

    # get houses robbed
    res = []
    i = len(decision) - 1
    curr_house = decision[i]
    #print(decision)
    while curr_house > -1:
        if len(res) == 0 or (res[-1] - curr_house) >= 2:
            res.append(curr_house)
        i -= 1
        curr_house = decision[i]
    print(res)

    res = []
    i = len(dec) - 1
    while i >= 2:
        if dec[i]:
            res.append(i-2)
            i -= 2
        else:
            i -= 1
    print(res)


    #print(len(res),res)
    return dp[-1]


print(max_profit_bot_up_dec(profit))