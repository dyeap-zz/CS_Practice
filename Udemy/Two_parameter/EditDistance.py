'''
#Given two strings A and B
choices
1. insert character
2. Replace character
3. delete character

A = GOAT
B = GET

output = 2
1. delete O and replace A with E

state
i - index of A
j - index of B
returns min num of operation to convert A to B
state transition
i,j = last index

ABC
BD
# only modify A
# base case
if i and j == -1: return max(distance of pointer to the end)
# recursive case either i and j have not reached the end
case 1: if both are equal = solve(i-1,j-1)
case 2: not equal
3 choices
# insert
in = 1+solve(i-1,j-1)
# replace
rep = 1+solve(i-1,j-1)
# delete
del = 1+solve(i-1,j)

recurrence relation?
BBC
BC

BABC
BC
solve(i,j) = min(in,rep,del)
'''
def edit_dist(A,B,i,j):
    # base case
    if i == -1 and j == -1:
        return 0
    if i == -1:
        return j+1
    if j == -1:
        return i+1
    # recursive case
    if A[i] == B[j]:
        return edit_dist(A,B,i-1,j-1)
    else:
        ins = 1+edit_dist(A,B,i,j-1)
        rep = 1+edit_dist(A,B,i-1,j-1)
        de = 1+edit_dist(A,B,i-1,j)
        return min(ins,rep,de)

A = "d"
B = "as"
print(edit_dist(A,B,len(A)-1,len(B)-1))


'''
Bottom up


1. dp size +1 row, col
2. base case 0,1,2... for row and col
3. bottom up alg
for i: 1-num_rows
    for j: 1-num_cols


bottom up equation

if A[i-1] == B[j-1]:
    dp[i][j] = dp[i-1][j-1]
else:
    ins = 1 + dp[i][j - 1]
    rep = 1 + dp[i - 1][j - 1]
    de = 1 + dp[i - 1][j]
    dp[i][j] = min(ins,rep,de)


top left

A = ABC
B = AD
cell = min num of operation to convert A to B given i and j
row = i and col = j
        -1  A   D
    -1  0   1   2
    A   1   0   1
    B   2   1   1
    C   3   2   2
'''
def min_edit_DP(A,B):
    num_rows = len(A)
    num_cols = len(B)
    # init dp table
    dp = [[float('inf') for _ in range(num_cols+1)]for _ in range(num_rows+1)]

    # init base case
    for i in range(num_rows+1):
        dp[i][0] = i

    for j in range(num_cols+1):
        dp[0][j] = j

    # DP algorithm
    for i in range(1,len(dp)):
        for j in range(1,len(dp[0])):
            # same letters
            if A[i - 1] == B[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            # different letters
            else:
                ins = 1 + dp[i][j - 1]
                rep = 1 + dp[i - 1][j - 1]
                de = 1 + dp[i - 1][j]
                dp[i][j] = min(ins, rep, de)
    return dp[-1][-1]

print(min_edit_DP(A,B))

