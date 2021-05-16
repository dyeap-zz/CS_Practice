# https://aonecode.com/interview-question/Count-Review-Combinations

'''
1. recursioin at each step have a choice of putting review in bag or not

like knapsack problem

states

num_rev(i,count_reviews_selected)

state transition
if crs == min_rev:
    res += 1
    crs -= 1

if i<0: ret 0
# if not less than 0 then

# can choose
init c = func(i-1,crs-1)
if rev(i) in range: c=func(i-1,crs-1)+1
# must try not choose
not_c=func(i-1,crs)

return c+not_s


bottom up:

1. num_states? + 1
2. start base case?  dp[0] = 0
3. alg?

dp[i] = dp[i-1,j] + if in range (dp[i-1,j-1]+1)
not in range(dp[i-1,j-1])
for (rev(i),nrc)
dp
min_rev = 2
len = 1-3
[1,2,4,3]
ans = 1,2  1,3 2,3
(i,nrc)
  0 1 2
0 0 0 0
1 0 1 0
2 0 2 2
3 0 2 2
4 0
all r/c = 0 -> 0

'''

'''
# idea to use
1. filter out all qualified reviews
2. start with [[]]. loop through all qualified reviews and add it to all combinations
3. if at any point you add and it exceeds what you want then you add res += 1
'''

#solution
def countTeams(num: int, skills, minAssociates: int, minLevel: int,
               maxLevel: int) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    qualified = []
    possible_teams = [[]]
    for a in skills:
        if minLevel <= a <= maxLevel:
            qualified.append(a)
    num_teams = 0
    while qualified: #[4,6,5,10]
        person = qualified.pop()
        new_teams = []
        for team in possible_teams:
            print(team)
            print(person)
            new_team = [person] + team
            print(new_team)
            if len(new_team) >= minAssociates:
                num_teams += 1
            new_teams.append(new_team)
        possible_teams += new_teams
        print(possible_teams)

    return num_teams


if __name__ == "__main__":
    num = 6
skills = [12, 4, 6, 13, 5, 10]
minAssociates = 3
minLevel = 4
maxLevel = 10
result = countTeams(num, skills, minAssociates, minLevel, maxLevel)
print(result)












'''

1. loop thru list find qualified  reviews
2. make a combination of each starting with [[]]

comb = [[]]
res = 0
3. loop: qual
    for c in comb:
        c.append(q)
        if len(c) > min length
            res += 1

        new_comb = c

'''