# https://aonecode.com/amazon-online-assessment-oa2/min-cost-to-repair-edges
# https://leetcode.com/discuss/interview-question/357310

def minCostToRepairEdges(n, edges, edgesToRepair):
    if n== 1: return -1
    if n == 0: return 0

    res = 0
    edgesToRepair.sort(key=lambda x: (x[2]))
    # every node is a parent of itself
    par = [i for i in range(n + 1)]


    # finds parent
    def find_par(node):
        if node == par[node]:
            return node
        return find_par(par[node])


    # make a as parent of b
    def union(n1, n2):
        par[find_par(n1)] = find_par(n2)


    # connect the given edges which have no cost
    for n1, n2 in edges:
        p1 = find_par(n1)
        p2 = find_par(n2)
        if p1 != p2:
            union(n1, n2)

    # connect if they have different different parents
    for n1, n2, cost in edgesToRepair:
        p1 = find_par(n1)
        p2 = find_par(n2)
        if p1 != p2:
            res += cost
            union(n1, n2)
    # find one parent and check if all nodes have the same parent else its not connected
    group = find_par(1)
    for i in range(1, n + 1):
        if find_par(i) != group:
            return -1
    return res