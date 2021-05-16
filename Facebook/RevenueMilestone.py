
input: array of revenues and milestones

revenues = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
milestones = [100, 200, 500]
output = [4, 6, 10]

Assume that milestones cannot be repeated

revenues_2 = [700, 800, 600, 400, 600, 700]
                0, 1,   2 ,   3,  4,    5
milestones_2 = [3100, 2200, 800, 2100, 1000]
                 0,  1 ,    2 ,   3,    4
expected_2 = [5, 4, 2, 3, 2]

dict = key: val

loop: milestone  n
    binarysearch through rev. log k

n*log(k)



milestones not sorted

binarysearch(tot,target)
    while smaller
        if target>=tot[mid]: return True
        # update mid
    retun False

loop: rev
    add all val

1. loop: milestone
2.    binarysearch



https://www.johncanessa.com/2021/01/07/revenue-milestones-in-java/