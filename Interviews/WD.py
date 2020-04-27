A = True
B = False
C = True

print(((~A)&(~B))&(B|C))


def partition(s):
    res = []
    dfs(s, [], res)
    return res


def dfs(s, path, res):
    if not s:  # backtracking
        res.append(path)
    for i in range(1, len(s) + 1):
        if isPar(s[:i]):
            dfs(s[i:], path + [s[:i]], res)


def isPar(s):
    return s == s[::-1]

partition("aacd")

for i in range(2,0,-1):
    print(i)
'''
def partition(s: str):
    dp = [[] for _ in range(len(s) + 1)]
    dp[-1] = [[]]
    for i in range(len(s) - 1, -1, -1):
        for j in range(i + 1, len(s) + 1):
            if s[i:j] == s[i:j][::-1]:
                for each in dp[j]:
                    dp[i].append([s[i:j]] + each)
    return dp[0]

partition("aac")
'''

# nums is a one-dimension array, like [1, 3, 0, 2] means
# first queen is placed in column 1, second queen is placed
# in column 3, etc.
def dfs(nums, index, path, res):
    if index == len(nums):
        res.append(path)
        return  # backtracking
    for i in range(len(nums)):
        nums[index] = i
        if valid(nums, index):  # pruning
            tmp = "." * len(nums)
            dfs(nums, index + 1, path + [tmp[:i] + "Q" + tmp[i + 1:]], res)



# check whether nth queen can be placed in that column
def valid(nums, n):
    for i in range(n):
        if abs(nums[i] - nums[n]) == n - i or nums[i] == nums[n]:
            return False
    return True

def solveNQueens(n):
    res = []
    dfs([-1] * n, 0, [], res)
    print(res)
    return res


solveNQueens(4)



class Solution:
    # @param s, a string
    # @return a list of lists of string
    # 1:30
    def partition(self, s):
        if not s:
            return []

        output = []
        self.findPartition(s, output, [])

        return output

    def findPartition(self, s, output, temp):
        if not s:
            output.append(temp[:])
            return

        for i in range(1, len(s) + 1):
            if self.isPalindrome(s[:i]):
                temp.append(s[:i])
                self.findPartition(s[i:], output, temp)
                temp.pop()

    def isPalindrome(self, string):
        return string == string[::-1]

sol = Solution()
sol.partition("aac")


SIZE = 3
solution = [[0]*SIZE for _ in range(SIZE)]
print(solution)

'''
def coinChange(coins, amount):
    if (amount < 0 or (len(coins) == 0 and amount >0)):
        return 0
    if (amount == 0):
        return 1
    return coinChange(coins[1:], amount) +  coinChange(coins, amount - coins[0])

print(coinChange([1,2],3))
'''

