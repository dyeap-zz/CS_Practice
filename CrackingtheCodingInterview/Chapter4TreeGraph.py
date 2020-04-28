class Solution:
    def word_break(self, s, words):
        d = [False] * len(s)
        for i in range(len(s)):
            for w in words:
                if w == s[i - len(w) + 1:i + 1] and (d[i - len(w)] or i - len(w) == -1):
                    d[i] = True
        return d[-1]

        return False

s = "leetcode"
wordDict = ["leet","code"]
sol = Solution()
print(sol.word_break(s,wordDict))

s = "1"
print(s[-5:-2])