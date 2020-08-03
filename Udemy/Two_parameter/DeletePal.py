'''
min number of deletes to get palindrome in string

idea:
aba za

caba
acba
abac

ab


state
i - left index
j - right index

should both pointers start in same place of opposite

return min number of delete to get palindrome

state transition


# base case
if one letter: return 0
# recursive case more than one letter


recurrenc relation
delete = 1+solve(i+1,j) or 1+solve(i,j-1)
if left == right:
    no_delete = solve(i+1,j-1)
solve(i,j) = min(delete,no_delete)

for idx_i: 0 to j
    for idx_j: len(S) to i
    if ends are equal:
        solve(i+1,j-1)
    else:
        1+solve(i,j)


            kazayake
             i    j

not equal                   equal - solve(i+1,j-1)
try deleting both ends
1+solve(i+1,j)
1+solve(i,j+1)

choices?
delete or not delete
# how to delete the middle character
# shifting and adding one is same as deleting

S = abca
    i  j
must delete from one of the ends. can only keep if the letters are the same
'''
S = "KAYAZKEWEF"
def min_del(S,i,j):
    # base case
    if i==j: return 0

    # recursive case
    res = float('inf')

    if S[i] == S[j]:
        res = min(res,min_del(S,i+1,j-1))
    else:
        res = min(res,1 + min(min_del(S,i + 1,j),min_del(S,i,j-1)))
    return res


print(min_del(S,0,len(S)-1))
'''
can flip
recurrence relation
no_delete = solve(i+1,j-1), if both sides are equal
dp[i][j] = dp[i-1][j-1]

delete = 1+solve(i+1,j) or 1+solve(i,j-1), if both sides not ==


solve(i,j) = min(delete,no_delete)

# dp table

1. dp size
2. base case diagonal left and bottom left cells are 0
3. alg/ bottom up equation

1. everything along diagonal are 0 for base case

abca

dp(i,j) = dp(i+1,j-1)

if diff:
    1+min(dp[i+1][j],dp[i][j-1])

if same:
    dp(i,j) = dp[i+1][j-1]

dp(1,2) = dp(0,1)

each cell is the min_del needed to get pal starting from i and ending in j

need a for loop that goes backwards
for i: 0 to len(S)
    for j: len(S) to i


  0 1 2
0 0 1 0
1 0 0
2 0 0 0

  a b c a
a 0 1 2 1
b   0 1 2
c     0 1
a       0

The key to answering the question quick is to write down what eac

abc


delete left side dp[i+1]

'''
def min_del_DP(S):
    num_cols = len(S)
    num_rows = len(S)
    # init dp table
    dp = [[0 for _ in range(num_cols)]for _ in range(num_rows)]

    # alg
    for i in range(num_cols-2,-1,-1):
        for j in range(i+1,num_rows,1):
            if S[i] == S[j]:
                dp[i][j] = dp[i+1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i+1][j],dp[i][j-1])
    #print(dp)
    return dp[0][-1]

print(min_del_DP(S))