'''
# 1. always have trianlge strucutre

# row above will always have less numbers

# recurrence relation
solve(i)
# base case
1. go through all i and give the min
# recursive case multiple row
res
1. for i in all rows:
    min(res,num[i]+solve(i,row below))
  [3]
 [1,0]
[2,4,6]
dp table
(index,row)
    0 1 2
0   5
1   3 2
2   2 4 6
formal definition

dp[i][j]=num[i][j] + min(dp[i-1][j-1:j+1])
1. initalize base case of last row

1. for row, interval = -1
2. for num_col,interval -1

1. get rough recursion solution
2. go through a smalll example to find formal recurrnece relation
3. write down notes on how you will apporach problem such as
starting point of algorithm, will you go through the entire table etc

'''




class Solution:
    def min_tri(self,tri):
        dp = [[float('inf') for _ in range(len(tri[-1]))] for _ in range(len(tri))]

        # initalize bottom row
        dp[-1] = tri[-1]

        # start algo
        for i in range(len(dp)-2,-1,-1):
            for j in range(len(tri[i])-1,-1,-1):
                #low = 0 if j < 0 else j
                dp[i][j] = tri[i][j] + min(dp[i+1][j:j+2])
        #print(dp)
        return min(dp[0])

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        return self.min_tri(triangle)