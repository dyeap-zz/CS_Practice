'''
find longest common subsequence

input is two strings
A = abc
B = zahbgc
output: longest common subsequence



states:
i - index string A
j - index string B

returns longest common subsequence between strings

EX:
A = "a"
B = "a"

state transitions:
start with i = len(A) and j = len(B)

base case
if i=-1 or j=-1: ""

recursive case i>=0 and j>=0
    if both pointers match: solve(i-1,j-1) + S[i]
    # dont match and not equal length decrement longer string
    # dont mathc and equal length


recurrence relation
solve(i,j) = max(solve(i,j),S[i] + solve(i+1,j+1)) i = 0,1,...,len(A), j = 0,1,...len(B)


        A="ab",B ="cac="

longer string dec

choices for every recursive call

res = ""
for i: 0 to len(A)
    for j: 0 to len(B)
        # try A
        if A[i] == B[j]
            # check if max
            S[i] + solve(i+1,j+1)

# always keep max string
'''
def lsq(A,B,i,j):
    # base case
    if i == -1 or j == -1: return ""

    # recursive case
    res = ""
    for idx_i in range(i,-1,-1):
        for idx_j in range(j,-1,-1):
            # check if ptrs are equal
            if A[idx_i] == B[idx_j]:
                pos = lsq(A,B,idx_i-1,idx_j-1) + A[idx_i]
                # check if it's larger
                if len(pos) > len(res):
                    res = pos
    return res

A = "ACHEFMGLP"
B = "XYCEPQMLG"

print(lsq(A,B,len(A)-1,len(B)-1))

# MEMOIZE
def lsq(A,B,i,j,dp):
    # base case
    if i == -1 or j == -1: return ""

    # recursive case
    if dp[i][j] != "": return dp[i][j]
    res = ""
    for idx_i in range(i,-1,-1):
        for idx_j in range(j,-1,-1):
            # check if ptrs are equal
            if A[idx_i] == B[idx_j]:
                pos = lsq(A,B,idx_i-1,idx_j-1,dp) + A[idx_i]
                # check if it's larger
                if len(pos) > len(res):
                    res = pos
    dp[i][j] = res
    return dp[i][j]

dp = [["" for _ in range(len(B))]for _ in range(len(A))]

#rows of A and rows of B
print(lsq(A,B,len(A)-1,len(B)-1,dp))
'''
bottom up approach:

1. size of dp cache +1
2. init base case don
3. alg/dp equation

small example:

A = "adb"
B  = "acb"
        B
    0   1    2
0   "a" ""  ""
1   ""  ""  ""  
2    
what is lsq(i=0,j=1), 
 
# base case ""


solve(i,j) = max(solve(i,j),S[i] + solve(i+1,j+1)) i = 0,1,...,len(A), j = 0,1,...len(B)

#not match = dp[i][j-1]
# need "" lining the beginning

dp[i][j] = max(S[i-1] + dp[i-1][j-1],dp[i-1][j]) i=1,2,...num_dp_rows, j=1,2,...num_dp_cols

if no match then dp[i][j] = max(dp[i-1][j],dp[i][j-1]
'''
def lsq_DP(A,B):
    # init dp table
    [["" for _ in range(len(B)+1)] for _ in range(len(A)+1)]

    # alg
    for i in range(1,len(dp)):
        for j in range(1,len(dp[0])):
            # matched
            # check if ptrs are equal
            if A[i-1] == B[j-1]:
                match = dp[i-1][j-1] + A[i-1]
                dp[i][j] = match
                # check if it's larger
                #if len(match) > len(dp[i-1][j]):
                #    dp[i][j] = match
                #else:
                #    dp[i][j] = dp[i-1][j]
            else:
                if len(dp[i-1][j]) > len(dp[i][j-1]):
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i][j-1]
    #print(dp)
    return dp[-1][-1]

print(lsq_DP(A,B))

# time complexity of recursion
