'''
# top down
class Solution(object):
    def numSquares(self, n):
        if n == 0: return 0
        if n == 1: return 1

        min_ways = n
        for i in range(1, n + 1):
            if (i * i <= n):
                way1 = self.numSquares(n - i * i)
                # way2 = self.numSquares(i*i)
                if (way1 + 1 < min_ways):
                    min_ways = way1 + 1
        return min_ways

# cached though too slow for leetcode still

class Solution(object):
    cache = {}

    def numSquares_helper(self, n):
        if n == 0: return 0
        if n == 1: return 1
        if n in self.cache: return self.cache[n]
        min_ways = n
        for i in range(1, n + 1):
            if (i * i <= n):
                way1 = self.numSquares_helper(n - i * i)
                if (way1 + 1 < min_ways):
                    min_ways = way1 + 1

        self.cache[n] = min_ways
        return self.cache[n]
'''
class Solution(object):
    def numSquares(self,n):
        dp = [None] * (n+1)
        dp[0] = 0
        dp[1] = 1
        for curr_n in range(1,n+1):
            curr_min = curr_n
            for i in range(1,int(curr_n**(1/2))+1):
                curr_min = min(curr_min,1+dp[curr_n-i*i])
            dp[curr_n] = curr_min
        return dp[n]


sol = Solution()
print(sol.numSquares(4))
nums = [1]
print(nums[2:])


def rob(self, nums):
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return 1
    return max(nums[0] + self.rob(nums[1:], self.rob(nums[1:])))