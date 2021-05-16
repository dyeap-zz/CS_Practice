# since max score is 100, you create a binning array

def countLevelUpPlayers(cutOffRank, num, scores):
    if cutOffRank == 0: return 0
    res = 0
    dp = [0 for _ in range(101)]
    for score in scores:
        dp[score] += 1

    # go backwards
    print(dp)
    r = 1
    for i in range(len(dp) - 1, -1, -1):
        res += dp[i]
        r += dp[i]
        if r > cutOffRank: break

    return res

cutOffRank = 3
num = 4
scores = [100,50,50,25]
print(countLevelUpPlayers(cutOffRank,num,scores))