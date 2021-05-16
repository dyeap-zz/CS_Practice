
def find(node, parents):
    if node == parents[node]: return node
    return find(parents[node], parents)


def minCostConnectNodes(N, connections):
    if N == 0: return 0
    parents = [i for i in range(0, N + 1)]

    edges = []
    for n1, n2, w in connections:
        edges.append([w, n1, n2])

    edges.sort()

    components = N
    res = 0

    for w, n1, n2 in edges:
        # get parents
        p1 = find(n1, parents)
        p2 = find(n2, parents)

        # check if they are in same component. if so then skip
        if p1 == p2: continue
        # not the same parents. connect the nodes together
        parents[p1] = p2
        res += w
        components -= 1
        if components == 1: return res

    return -1


use kruskals

sort everything by edge weight.




union find everything