'''
# Incorrect solution where the subproblem is not contained because of nums[index] < nums[index + 1]. Don't
have access to num[index+1] need to pass it through
class Solution:
    cache = {}
    def lengthOfLIS_helper(self, nums, index):
        # base case
        if index == len(nums): return 1
        # if index == len(nums)-1: return 1
        # guaranteed one number

        taken = 0
        if index + 1 < len(nums) and nums[index] < nums[index + 1]:
            taken = 1 + self.lengthOfLIS_helper(nums, index + 1)

        nottaken = self.lengthOfLIS_helper(nums, index + 1)
        if index == 1:
            print(taken,nottaken)
        self.cache[index] = max(taken, nottaken)
        return self.cache[index]

    def lengthOfLIS(self, nums) -> int:
        res = self.lengthOfLIS_helper(nums, 0)
        return res
'''
# correct solution that contains value
class Solution:
    cache = {}
    def lengthOfLIS_helper(self, nums, prev_num, index):
        # base case
        if index == len(nums): return 0

        # guaranteed one number
        taken = 0
        if prev_num < nums[index]:
            taken = 1 + self.lengthOfLIS_helper(nums,nums[index], index + 1)

        nottaken = self.lengthOfLIS_helper(nums,prev_num, index + 1)
        if index == 1:
            print(taken,nottaken)
            
        self.cache[index] = max(taken, nottaken)
        return self.cache[index]

    def lengthOfLIS(self, nums) -> int:
        res = self.lengthOfLIS_helper(nums,float('-inf'), 0)
        return res

# memoized solution
class Solution:
    # cache = {}
    def lengthOfLIS_helper(self, nums, prev_num, index, cache):

        # base case
        if index == len(nums): return 0

        # guaranteed one number
        if (prev_num, index) in cache:
            return cache[(prev_num, index)]

        taken = 0
        if prev_num < nums[index]:
            taken = 1 + self.lengthOfLIS_helper(nums, nums[index], index + 1, cache)

        nottaken = self.lengthOfLIS_helper(nums, prev_num, index + 1, cache)

        cache[(prev_num, index)] = max(taken, nottaken)
        return cache[(prev_num, index)]

    def lengthOfLIS(self, nums) -> int:
        res = self.lengthOfLIS_helper(nums, float('-inf'), 0, {})
        return res

# incorrect DP solution. Does not account for test case [2,5,3,4]
def lengthOfLIS_helper(nums):
    res = 0
    for start in range(len(nums)):
        prev = nums[start]
        lis = 1
        for end in range(start+1,len(nums)):
            if prev < nums[end]:
                lis += 1
                prev = nums[end]
        res = max(res,lis)
    return res
# can't find answer to larger one without first doing the others
# correct solution for dp
class Solution:
    def lengthOfLIS(self, nums) -> int:
        if len(nums) == 0: return 0
        dp = [1] * len(nums)
        for start in range(len(nums)-1,-1,-1):
            for i in range(start+1,len(nums)):
                if nums[start] < nums[i]:
                    dp[start] = max(dp[start],dp[i]+1)
        #print(dp)
        return max(dp)

# correct solution for dp starting in the beginning
class Solution:
    def lengthOfLIS(self, nums) -> int:
        if len(nums) == 0: return 0
        dp = [1] * len(nums)
        for end in range(len(nums)):
            for start in range(end):
                if nums[start] < nums[end]:
                    dp[end] = max(dp[end],dp[start]+1)
        return max(dp)
    
[1,2,1,1,2,3]

#[3,1,3,3,2,1]

# t1
#arr = [10,9,2,5,3,7,101,18]
# output = 4
# t2
arr = [4,10,4,3,8,9]
# output = 3
sol = Solution()
print(sol.lengthOfLIS(arr))
print(sol.cache)

