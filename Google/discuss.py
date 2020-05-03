'''
#https://leetcode.com/discuss/interview-question/363871/Google-or-Memorize-Phone-Number

in: [1,2,3,4,5,8]

max_quality
# base case
if bad: return 0
if excellent: return 2
if good: return 1

try 2 and 3
# recursion
two = max_qual(nums[0:2]) + max_qual(num[2:])
three = max_qual(nums[0:3]) + max_qual(num[3:])
max(two,three)

store res

dict{tup of group:max quality}

bottom up

1. subproblem - max_quality(between two/group)
2. math - above

base case
0 0
_ _ _ _
0 1 2 3

nums = [1,2,3,4,5]
dp = [0] * (n+2)
dp[0] = 0
dp[1] = egu(nums[0:2])
dp[2] = egu(nums[0:3])
dp[3] = dp[1] + nums[2:4]

for curr_n in range(4,n):
    # get two
    two_qual = egu(nums[curr_n-1:curr_n+1])
    three_qual = egu(nums[curr_n-2:curr_n+1])
    dp[i] = max(two_qual + dp[curr_n - 2], three_qual + dp[curr_n - 3])

return dp[n]

# got the rough draft idea
'''