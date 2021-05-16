import heapq


def maxPathScore(matrix):
    n = len(matrix)
    m = len(matrix[0])
    vis = set()

    inc_r = [0, 0, -1, 1]
    inc_c = [-1, 1, 0, 0]

    h = [(-matrix[0][0], 0, 0, matrix[0][0])]
    # heapq.heapify(h)
    vis.add((0, 0))

    while h:
        print(h)
        curr_ele, r, c, min_ele = heapq.heappop(h)

        if r == n - 1 and c == m - 1: return min(min_ele, matrix[r][c])

        for i in range(len(inc_r)):
            mv_r = r + inc_r[i]
            mv_c = c + inc_c[i]

            if (0 <= mv_r <= n - 1 and 0 <= mv_c <= m - 1 and (mv_r, mv_c) not in vis):
                tup_ele = (-matrix[mv_r][mv_c], mv_r, mv_c, min(min_ele, matrix[mv_r][mv_c]))
                heapq.heappush(h, tup_ele)
                vis.add((mv_r, mv_c))

    return -1


matrix = [[7, 5, 3], [2, 0, 9], [4, 5, 9]]
print(maxPathScore(matrix))







# max heap

(ele,r,c,minele)
put in top right node.

vis = set
while h:
    if at the end: return

    loop all dir:
        put in not if not vis
            min(miele,curr_ele)