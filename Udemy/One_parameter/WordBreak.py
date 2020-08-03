'''
output the number of ways to break up word into words in dictionary

dictionary stores all valid words.

The entire word must be broken down to count
and allowed to reuse words


word = abca b
2 choices either break or not break word


    abcab
 break - if right side is in D     dont break - check if this word is in
abca b                               abcab,3

abca                                  abc ab,2   abcab,2

D = ["ab","cab","b","abcab"]


S = abc

                 abc,2
    ab c,1                   abc,1

a b c,0   ab c,0           a bc,0       ab c,0

1. states
the index of the word that is being broken - i
return the number of ways to break word at particular index

2. state transitions

start with i = 0 or i = last char
i = last char
num_way(S,D,i)

# base case
if i = 0 and S is in dict: ret 1

reccurrence relation


if word from i to end in D:
    break = num_ways(S[:i],D,i-1)

not_break = num_ways(S,D,i-1)

recurrence relation
num_ways(i) = not_break+break
'''
# recursive solution
def num_ways(S,D,i):
    # base case
    if i == 0:
        if S in D: return 1
        else: return 0
    # recrusive case
    r_wrd = S[i:]
    brk = 0
    if r_wrd in D:
        brk = num_ways(S[:i],D,i-1)
    nt_brk = num_ways(S,D,i-1)
    return brk + nt_brk


S = "abcd"
D = ["ab","c","b","a","bc","d","cd"]
S = "pineapplepenapple"
D = ["apple","pen","applepen","pine","pineapple"]
print(num_ways(S,D,len(S)-1))

'''
abc,2

abc,1
# use one state
i - last index of last char inside S 0-i

# base case
if S == -1: return 0
# recrusive case i > len(S)
for char in string go back:
    if S[i:end] in D:
        numway(i-1)

a b d
'''
# only using one parameter
def num_ways(S,D,i):
    # base case
    if i == -1: return 1
    # recursive case
    res = 0
    for j in range(i,-1,-1):
        if S[j:i+1] in D:
            res += num_ways(S,D,j-1)
    return res

print(num_ways(S,D,len(S)-1))

# memoize
def num_ways(S,D,i,dp):
    # base case
    if i == -1: return 1
    # recursive case
    if dp[i] != -1: return dp[i]
    res = 0
    for j in range(i,-1,-1):
        if S[j:i+1] in D:
            res += num_ways(S,D,j-1,dp)
    dp[i] = res
    return res

dp = [-1] * len(S)
print(num_ways(S,D,len(S)-1,dp))

'''
# bottom up
turn into bottom up equation


1. dp array how large? dp = len() + 1
2. how to init base case? dp[0] = 1
3. how to iterate?

init dp array +1

use 0 as 1

abc

dp = [1,-1,-1,-1]
bottome up equation

for j in range(i, -1, -1):
    if S[j:i + 1] in D:
        res += num_ways(S, D, j - 1, dp)

dp[i] = sum(dp[j-1])

a b c 
ab 

ab c

dp = [1,1,2,2]

abc
i = 2
j = 2
for i: 0 to len(S)
    for j: 0 to i+1
        if S[j:i+1]:
            dp[i] += dp[j-1]
'''
def num_ways_BU(S,D):
    # init dp array
    dp = [0] * (len(S) + 1)

    # store base case
    dp[0] = 1

    for i in range(len(S)):
        for j in range(1,i+1):
            if S[j-1:i+1] in D:
                dp[i+1] += dp[j-1]
    #print(dp)
    return dp[-1]

print(num_ways_BU(S,D))

# below is a better way. You just copy what you had and then modify how you index it
# because you need to store the base case
'''
for i in range(1,N+1):
for j in range(i, -1, -1):
    if S[j:i + 1] in D:
        res += num_ways(S, D, j - 1, dp)

'''
'''
S = "pineapplepenapple"
D = ["apple","pen","applepen","pine","pineapple"]

        p,i,n,e,a,p,p,l,e,p,e,n,a,p,p,l,e
dp = [1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0]
'''