# https://aonecode.com/path-with-maximum-minimum-value-1

'''
1. dynamic programming

states(i,j)
return given i,j the max score is min_integer along path

state transition

base case:
    if reach BR: return min(func(i-1,j), func(i,j-1), matrix[i][j])

dp[i,j] = min(max(dp[i-1,j],dp[i,j-1]),matrix[i,j])

base_case_size:

alg
'''

def maxPathScore(matrix):
    dp = [[-1 for col in range(len(matrix[0]))] for row in range(len(matrix))]
    dp[0][0] = matrix[0][0]
    # alg
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if (i == 0 and j == 0): continue
            # print("i=%d,j=%d"%(i,j))
            if j == 0:
                dp[i][j] = min(dp[i - 1][j], matrix[i][j])
            elif i == 0:
                dp[i][j] = min(dp[i][j - 1], matrix[i][j])
            else:
                curr_path = max(dp[i - 1][j], dp[i][j - 1])
                dp[i][j] = min(curr_path, matrix[i][j])

    return dp[-1][-1]

matrix = [[0, 1], [0, 2], [1, 3], [2, 3], [2, 5], [5, 6], [3, 4]]
maxPathScore(matrix)