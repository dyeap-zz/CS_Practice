def dfs(root, out, inc, vis, res):
    # base case
    if root in vis: return
    if root in inc: return
    # recursive case - not visited and no inc
    res.append(root)
    vis.add(root)
    neis = list(out[root])
    for nei in neis:
        if nei in vis: continue
        out[root].remove(nei)
        inc[nei].remove(root)
        if len(out[root]) == 0: del out[root]
        if len(inc[nei]) == 0: del inc[nei]
        dfs(nei, out, inc, vis, res)
    return

from collections import defaultdict
def findOrder(numCourses: int, prerequisites):
    out, inc = defaultdict(set), defaultdict(set)
    for a, b in prerequisites:
        out[b].add(a)
        inc[a].add(b)

    vis = set()
    res = []
    for node in range(numCourses):
        if node not in inc:
            dfs(node, out, inc, vis, res)

    return res if len(res) == numCourses else []

n = 4
pre = [[1,0],[2,0],[3,1],[3,2]]
print(findOrder(n,pre))