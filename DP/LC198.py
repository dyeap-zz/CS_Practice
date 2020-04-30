# top down
class Solution(object):
    def rob(self, nums):
        if len(nums) == 0:
            return 0

        return max((nums[0]+self.rob(nums[2:])),(self.rob(nums[1:])))

# caching

class Solution(object):
    cache = {}
    def rob(self, nums):
        cache = self.cache
        if len(nums) == 0:
            return 0
        tup_nums = tuple(nums)
        if tup_nums in cache: return cache[tup_nums]
        cache[tup_nums] = max((nums[0]+self.rob(nums[2:])),(self.rob(nums[1:])))
        return cache[tup_nums]

# DP

class Solution(object):
    def rob(self, nums):
        if len(nums) == 0: return 0
        dp = [0] * (len(nums))
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            if i - 2 < 0:
                curr_max = nums[i]
            else:
                curr_max = nums[i] + dp[i - 2]

            dp[i] = max(curr_max, dp[i - 1])

        return dp[-1]