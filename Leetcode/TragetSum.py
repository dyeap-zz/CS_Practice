'''
You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.

Example 1:

Input: nums is [1, 1, 1, 1, 1], S is 3.
Output: 5
Explanation:

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.
'''
This is a DP problem.
#DFS - backtracking
Will try and find a top down approach


states
curr_sum - sum we currently have
i - we are going to use
return number of ways given a curr sum and i

transition - start with curr_sum = S and i = 0
# base case
if i == -1: ret 0
if i ==-1 and sum == 0: ret 1
# recursive case sum > 0  and i < last index+1
#choices either add or subtract
add = num_ways(sum-num[i],i-1)
sub = num_ways(sum+num[i],i-1)


recurrence relation
num_ways(sum,i) = num_ways(sum - num[i], i - 1) + num_ways(sum+num[i],i-1)

DP solution:
1. size of DP table - same as len(nums) and S
2. how to init base case - init first row for all matching numbers
3. alg -

num = [1,1,1,1,1], S = 3

row = index, col = sum

if it goes off grid = 0
    0     1     2   3   4   5
0   1     0     1   0   0   0      base case
1   1     0     1   0   0   0
2   0     2     0   1   0   0
3   2     0     3   0   1   0
4   0     2     0   4
num_ways(sum,i) = num_ways(sum - num[i], i - 1) + num_ways(sum+num[i],i-1)
dp[i,j] = dp[i-1,j-num[i]] + dp[i-1,j+num[i]]

for i: 1 to S
    for j: 0 to num_rows
        if you get out of bound of grid: 0
        dp[i,j] = dp[i-1,j-num[i]] + dp[i-1,j+num[i]]

-1000 to 0 is +1000

def num_ways(nums,S):
    num_rows = len(nums)
    num_cols = 2001
    # create dp table
    dp = [[0 for _ in range(num_cols)] for _ in range(num_rows)]

    # base case
    for j in range(num_cols):
        if -(nums[0]+1000) or (nums[0]+1000) == j:
            dp[0][j] = 1

    # alg
    for i in range(1,num_rows):
        for j in range(num_cols):
            #add, sub = 0, 0
            # check the bounds
            sub_idx, add_idx = j-nums[i], j+nums[i]
            sub = dp[i-1][sub_idx]
            add = dp[i-1][add_idx]
            # update dp[i,j]
            dp[i][j] = add + sub

    return dp[-1][S+1000]