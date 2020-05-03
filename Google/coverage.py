#https://leetcode.com/discuss/interview-question/601397/Google-Phone-Interview

# min number of coverage
# must be O(n) time

# always choose the max?

2 1 2

2 1 1 1
# recursion
1. what is subproblem?
min_num coverage to get cover arr up to that point



min_cov()
if len(num) == 1: return nums = 1 if nums[0]>1

right_min = min_cov(nums[1:])


dp[n]

1  1  2  1 1


dp = [1]

for num in nums:
    dp[i] = dp[i-arr[]]