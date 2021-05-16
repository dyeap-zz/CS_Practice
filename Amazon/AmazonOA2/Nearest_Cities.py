#https://aonecode.com/amazon-online-assessment-nearest-cities

# https://leetcode.com/discuss/interview-question/872961/Amazon-or-OA-2020-or-Nearest-City


import math


def compute_dist(x1, x2, y1, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def findNearestCities(numOfPoints: int, points: List[str], xCoordinates: List[int], yCoordinates: List[int],
                      numOfQueriedPoints: int, queriedPoints: List[str]) -> List[str]:
    n = numOfQueriedPoints
    d = [[0 for row in range(n)] for col in range(n)]
    min_dist = float('inf')
    min_point = None
    res = []

    for r in range(n):
        for c in range(n):
            # skip same points
            if r == c: continue
            dist = compute_dist(xCoordinates[r], xCoordinates[c], yCoordinates[r], yCoordinates[c])
            # if two points have same distance
            if dist == min_dist:
                min_point = None
            elif dist < min_dist:
                min_dist = dist
                min_point = points[c]
        res.append(min_point)

    return res




# lessons write out output first
# write english logic first to make it easier








1. need to find all other xnei. get the closest one and compute euclida dist
2. need to find all other ynei. get the closest one and compute euclida

take the min(1/2 and that's your answer)




if need product name

get all points along x

xcoor:(xnei name of all points shared along xcoor)
xname:(xcoor,ycoor)

same with y

loop: names of query
    use xcoor and get all neigh
    use ycoor and get all nei

    if both no coor:continue

    min dist = inf

    loop xnei:
        pull out x,y from xy_name
        compute dist and same min_val

    loop ynei:
        compute dist and same min_val





dict{product name: }

xdict