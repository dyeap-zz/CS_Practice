'''
There are n rows of houses, each house can be painted with one of the three colors: R,G, or B.
The cost of painting each house with a certain color is different. You have to paint all houses
such that no two adj houses have the same color. What is min cost?

cost[][] =
[red, blue, green]

follow all steps
time and space
find tabular solution

1. states -
color,0-2 - 0 = red, 1 = blue, 2 = green
house, i -

cost function
min cost to paint house

2. transition
solve(color,house)
# base case
if no house: return cost 0
if one house?
# recursive case more 1 or more houses
for all colors:
    if same color than prev: skip
    else:
        solve(curr_color,house)
return min_cost

Have a for loop for different colors of the houses
rbg

r b/g (rg)/(b/g)

recurrence relation
solve(color,house) = cost[i] + min(solve(colors[i],i))

3. write the recursive function
'''

def min_cost(cost,prev_color,i):
    # base case
    if i == -1: return 0
    # recursive case
    res = float('inf')
    for paint in [0,1,2]:
        # adj color house check
        if paint == prev_color: continue
        else:
            res = min(res,cost[i][paint] + min_cost(cost,paint,i-1))
    return res


cost = [[17,2,17],
        [16,16,5],
        [14,3,9]
]
print(min_cost(cost,-1,len(cost)-1))

# memoize the solution
#Use a 2D grid and store the prev_color and i(house)

def min_cost(cost,color,i,dp):
    # base case
    if i == -1: return 0
    # recursive case
    # check if in cache
    if i >=0 and dp[color][i] != float('inf'): return dp[color][i]

    res = float('inf')
    for paint in [0,1,2]:
        # adj color house check
        if paint == color: continue
        else:
            res = min(res,cost[i][paint] + min_cost(cost,paint,i-1,dp))
    dp[color][i] = res
    return dp[color][i]

num_house = len(cost)
num_colors = 3
dp = [[float('inf') for _ in range(num_house)] for _ in range(num_colors)]
print(min_cost(cost,-1,len(cost)-1,dp))

# bottom up approach
#Try an example
# base case first?
#inc? dec?
'''
Have to do base case first

have this i-1 we need to work with so for i 0

subproblem?
What the min cost at a particular color house

row = color
col = house or index

1. go down the row for base case and init for first house paint it all possible color

dp table

(color,house)
    0   1   2
0   17  18  47
1   2   33  21
2   17  102 27

change the recurrence relation to bottom up equation

dp[color][house] = min(dp[color][house], cost[color][house] + dp[~color][house-1])
for house 1-n_houses
    for colors

'''
def paint_botup(cost):
    # init the dp table
    dp = [[float('inf') for _ in range(num_house)] for _ in range(num_colors)]

    # init the base case for first house
    first_house = 0
    #for colors in cost[0]:
        #print(colors)
    for color,price in enumerate(cost[0]):
        #print(color,price)
        dp[color][0] = price

    #print(dp)
    #print(cost)
    #res = float('inf')
    # start with next column house and do computation
    for h in range(1,len(cost)):
        for c in range(3):
            # need to get the smaller value of the other colors
            for prev_c in range(3):
                if prev_c == c: continue
                else:
                    dp[c][h] = min(dp[c][h],cost[h][c] + dp[prev_c][h-1])
                    #res = min(res,dp[c][h])

    res = float('inf')
    for color in range(3):
        res = min(res,dp[color][-1])
    return res



#print(cost)
print(paint_botup(cost))


# get the recurrence relation correct
# try to line up grid same as the data structure
# do you need a for loop at the end to go across the results?


#To find the color of the houses you painted use another cache that stores the previous color
#house.

#size of cache will be same as size of dp table


def paint_botup(cost):
    # init the dp table
    dp = [[float('inf') for _ in range(num_house)] for _ in range(num_colors)]
    prev_color = [[-1 for _ in range(num_house)] for _ in range(num_colors)]

    # init the base case for first house
    for color,price in enumerate(cost[0]):
        #print(color,price)
        dp[color][0] = price

    # start with next column house and do computation
    for h in range(1,len(cost)):
        for c in range(3):
            # need to get the smaller value of the other colors
            for prev_c in range(3):
                if prev_c == c: continue
                else:
                    if cost[h][c] + dp[prev_c][h-1] < dp[c][h]:
                        prev_color[c][h] = prev_c
                    dp[c][h] = min(dp[c][h],cost[h][c] + dp[prev_c][h-1])
                    # using the new paint then log it in

                    #res = min(res,dp[c][h])

    res = float('inf')

    for color in range(3):
        res = min(res,dp[color][-1])

    # find min house color
    min_color = -1
    for color in range(3):
        if dp[color][-1] == res:
            min_color = color

    house_color = [-1 for _ in range(len(cost))]
    house_color[-1] = min_color
    for h in range(len(cost)-1,0,-1):
        #print(h,min_color)
        house_color[h-1] = prev_color[min_color][h]
        min_color = house_color[h-1]

    print(house_color)
    return res



print(paint_botup(cost))
'''
n is number of houses
m is number of colors

recursion top down
time - O(3*2^n)
space - O(1)

bottom up
time - O(n*m^2)
space - O(n*m)

Solution:
min_cost(i,)


improvements

could have tried store the base case of 0 in the table. So i = 1 means house index of 0
'''