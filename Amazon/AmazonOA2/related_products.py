'''
union find to get all the components.

make graph -> defaultdict(set)

dfs one node. put it in visited.

res = 0
num_nodes_visited = 0
loop nodes.
    if no visited:
        dfs() store number of nodes in that components
        found = len(vis) - num_nodes_visited
'''

from collections import defaultdict


def findLargestGroup(items):
    def dfs(node,vis,g,cv):
        print("node  =%s"%node)
        if node in vis:
            return
        vis.add(node)
        cv.add(node)
        for nei in g[node]:
            dfs(nei,vis,g,cv)

    g = defaultdict(set)
    nodes = set()
    for edges in items:
        for i in range(1, len(edges)):
            n1 = edges[i]
            n2 = edges[i - 1]
            g[n1].add(n2)
            g[n2].add(n1)
            nodes.add(n1)
            nodes.add(n2)
    res = []
    vis = set()
    num_node_vis = 0
    print(g)
    for node in nodes:
        print(node)
        if node not in vis:
            cv = set()
            dfs(node,vis,g,cv)
            #f = len(vis) - num_node_vis
            #print("f = %d"%f)
            if len(cv) > len(res):
                res = list(cv)
    res.sort()
    #if len(res) == 6:
    #    res[3], res[4] = res[4], res[3]
    return res
g = [["product1","product2","product3"],
     ["product5","product2"],
     ["product6","product7"],
     ["prodcut8","product7"]]
print(findLargestGroup(g))