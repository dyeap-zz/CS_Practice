'''
1.	Define the state -  states, cost function, return?
2.	List out all state transitions
3.	Implement a recursive solution
4.	Memoize
5.	Make it bottom up
'''
'''
2 states/inputs

1. weight of back, w
2. item being considered, i

func = ks(w,i)
return max_profit of contents in bag

state transition

base case
weight < 0, w=0 : 0
no item in back, i<0 = 0

recursive case
Either take the item or do not take it

1. include the item or do not include it

ks(w,i) = inc - val[i] + ks(w-weight[i],i-1) or exc - ks(weight[i],i-1)
optimal - max(inc,exc)

recurrence relation
ks(w,i) = max(inc,exc)

if have space: weight <= W
    ks(w,i) = max(inc,exc)
else: # no space
    exc

ks(0,i) = 0
ks(w,-1) = 0

rec
'''

def knapsack_DP(W, weights, values):
    dp = [[0 for i in range(0, len(weights) + 1)] for j in range(0, W + 1)]
    dp[W][0] = 0
    dec = [[False for _ in range(0,len(weights)+1)] for _ in range(0,W+1)]
    for i in range(1, len(weights) + 1):
        for w in range(0, W + 1):
            if weights[i - 1] <= w:
                include = dp[w - weights[i - 1]][i - 1] + values[i - 1]
                exclude = dp[w][i - 1]
                dp[w][i] = max(exclude, include)
                if include > exclude:
                    dec[w][i] = True

            else:
                dp[w][i] = dp[w][i - 1]

    print(dec)
    #print(len(weights))
    col = len(weights)
    wei = W
    while col > 0 and wei > 0:
        #print(wei,col)
        if dec[wei][col] == False:
            col -= 1
        else:
            print(weights[col-1],values[col-1])
            wei -= weights[col-1]
            col -= 1

    return dp[W][len(weights)]



weights = [3, 7, 10, 6]
values = [4, 14, 10, 5]
W = 20
N = len(weights)

print(knapsack_DP(W, weights, values))