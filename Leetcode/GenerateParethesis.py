'''
class Solution:
    def gen_comb(self, o, n, path, res):
        # base case
        if n == 0 and o == 0 : return
        if len(path) == n * 2:
            res.append(path)
        # recursive case
        if o == 0:
            self.gen_comb(self, o + 1, n - 1, path + "(", res)
        elif o > 0:
            if n > 0:
                self.gen_comb(o + 1, n - 1, path + "(", res)
            else:
                self.gen_comb(o, n, path + ")", res)

    def generateParenthesis(self, n: int):
        res = []
        self.gen_comb(1, n, "(", res)
        return res
sol = Solution()
print(sol.generateParenthesis(2))
'''
class Solution:
    def gen_comb(self,S,o,c,path,res):
        # base case
        if o < 0 or c < 0: return
        if o == 0 and c == 0:
            res.append(path)
        # recursive case
        self.gen_comb(S,o-1,c,path+"(",res)
        self.gen_comb(S,o,c-1,path+")",res)


    def generateParenthesis(self, n: int):
        res = []
        self.gen_comb("",n-1,n,"(",res)
        return res

sol = Solution()
print(sol.generateParenthesis(2))