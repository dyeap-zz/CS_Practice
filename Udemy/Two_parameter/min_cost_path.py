'''
# states
row, col

cost function - return the min cost to get to row,col

can only move down and right - must try all combination of down and right
# state transition
start with row=0,col=0
min_cost(grid,row,col)
# base case
if reach invalid row: ret inf
if reach invalid col: ret inf
# recursive case
return curr_cost + min(down,right)


recurrence relation
down = min_cost(row+1,col)
right = min_cost(row,col+1)
min_cost(row,col) = grid[row][col] + min(down,right)
'''
# how to deal with it when row and col are not valid
# if you can either go down or right

# input
grid = [[1,1,4],
        [9,100,1],
        [1,1,100],
        [1,1,1]
]
# recursive case
def min_cost(grid,row,col):
    # base case
    if row >= len(grid): return float('inf')
    if col >= len(grid[0]): return float('inf')
    if row == len(grid)-1 and col == len(grid[0])-1: return grid[-1][-1]
    # recursive case can make a move
    down = min_cost(grid,row+1,col)
    right = min_cost(grid,row,col+1)
    return grid[row][col] + min(down,right)

print(min_cost(grid,0,0))

# memoize
def min_cost(grid,row,col,dp):
    # base case
    if row >= len(grid): return float('inf')
    if col >= len(grid[0]): return float('inf')
    if row == len(grid)-1 and col == len(grid[0])-1: return grid[-1][-1]
    # recursive case can make a move
    if dp[row][col] != -1: return dp[row][col]
    down = min_cost(grid,row+1,col,dp)
    right = min_cost(grid,row,col+1,dp)
    dp[row][col] = grid[row][col] + min(down,right)
    return dp[row][col]

num_col = len(grid[0])
num_row = len(grid)
dp = [[-1 for _ in range(num_col)] for _ in range(num_row)]

print(min_cost(grid,0,0,dp))

'''
# bottom up approach

size of dp? +1
how to init base case? 
dp eqution?

for row: len(grid) to 0
    for col: len(grid[0]) to 0
        

down = dp(r+1,c)
right = dp(r,c+1)
dp[r][c] = grid(r,c) + min(down,right)

for base case line the bottom and right side with inf and bot right with 0
    
1. create dp table
2. all of last row and col will be inf
3. dp[-1][len(dp)-1] = 0
4. col, row

grid = [[1,3,1], 
        [3,100,1],
        [1,1,1]  
    
]

dp = [
[7,6,3,X]
[6,102,2,X]
[3,2,1,0]
[X,X,0,0]    
]
'''
# recursion time complexity is O(4^n)

# O(2^N) for the recursion decisions
# the height of the tree is 2N. The worst case is go all the way right then all the way down
# which is N+N or (N+M)
# thus O(2^(height of tree)) = O(2^2N) = O(4^N)
# normally number of nodes 2^h - 1 where h=1,2,3,...N

def min_cost_DP(grid):
    num_col = len(grid[0])
    num_row = len(grid)
    dp = [[0 for _ in range(num_col+1)]for _ in range(num_row +1)]

    # init base case
    for j in range(num_col-1):
        dp[-1][j] = float('inf')

    for i in range(num_row-1):
        dp[i][-1] = float('inf')

    # algorithm
    for r in range(num_row-1,-1,-1):
        for c in range(num_col-1,-1,-1):
            dp[r][c] = grid[r][c] + min(dp[r+1][c],dp[r][c+1])

    return dp[0][0]


print(min_cost_DP(grid))

# to reconstruct the solution we have a dec that states if we took right or down
# did we go right? 0 = down 1 = right
def min_cost_DP(grid):
    num_col = len(grid[0])
    num_row = len(grid)
    dp = [[0 for _ in range(num_col+1)]for _ in range(num_row +1)]
    dec = [[0 for _ in range(num_col)] for _ in range(num_row)]

    # init base case
    for j in range(num_col-1):
        dp[-1][j] = float('inf')

    for i in range(num_row-1):
        dp[i][-1] = float('inf')

    # algorithm
    for r in range(num_row-1,-1,-1):
        for c in range(num_col-1,-1,-1):
            d = dp[r+1][c]
            rght = dp[r][c+1]
            if rght < d:
                dec[r][c] = 1
            dp[r][c] = grid[r][c] + min(dp[r+1][c],dp[r][c+1])


    res = []
    i,j = 0,0
    #print(dec)
    while i < len(dec) and j < len(dec[0]):
        if i == len(dec)-1 and j == len(dec[0])-1: break
        if dec[i][j] == 1:
            res.append("r")
            j += 1
        else:
            res.append("d")
            i += 1
    print(res)
    return dp[0][0]

print(min_cost_DP(grid))
