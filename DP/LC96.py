# top down recursion
class Solution:
    def numTrees(self, n: int) -> int:

        if n == 0: return 1
        if n == 1: return 1

        ways = 0
        for root in range(1, n + 1):
            left = self.numTrees(root - 1)
            right = self.numTrees(n - root)
            ways += left * right
        return ways

# cached
class Solution:
    cache = {}
    def numTrees(self, n: int) -> int:
        if n==0: return 1
        if n==1: return 1
        if n in self.cache: return self.cache[n]
        ways = 0
        for root in range(1,n+1):
            left = self.numTrees(root-1)
            right = self.numTrees(n-root)
            ways += left * right
        self.cache[n] = ways
        return self.cache[n]
# dp

class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[0] = 1
        dp[0] = 1
        for level in range(1,n+1):
            ways = 0
            for root in range(1,n+1):
                left = dp[root-1]
                right = dp[level-root]
                ways += left * right
            dp[level] = ways
        return dp[n]

# dp in which dp are shifted up by one
class Solution(object):
    def rob(self, nums):
        if len(nums) == 0: return 0
        dp = [0] * (len(nums) + 1)
        dp[0] = 0
        dp[1] = nums[0]
        for i in range(2, len(nums) + 1):
            dp[i] = max(nums[i - 1] + dp[i - 2], dp[i - 1])

        return dp[-1]

word = ""

print(word[0::2])