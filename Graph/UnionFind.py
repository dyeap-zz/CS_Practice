'''
Union Find is method of determining if two nodes are in the same graph

Can generally be done on nodes that are letter strings or numbers.

Amotized
time is O(1) - to determine if two nodes are in the same set

space(n)-number of nodes

It uses an array to store its parent.

1. all nodes start conneced to itself
2. for both nodes find topmost parent
3. only need to connect one of the parents together
4. iterate until node equal itself

to check if connected run find and see if the same parent


node 1 2 3
pare 1 1 2

1-2

3
'''

'''
def findRedundantConnection(self, edges):
    parent = [0] * len(edges)

    def find(x):
        if parent[x] == 0:
            return x
        parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        rootX = find(x)
        rootY = find(y)
        if rootX == rootY:
            return False
        parent[rootX] = rootY
        return True

    for x, y in edges:
        if not union(x - 1, y - 1):
            return [x, y]

    raise ValueError("Illegal input.")
'''


edge = [1,2], n = num_nodes
parent = [0] * n

def find(node,parent):
    if node == parent[node]: return node
    return find(parent[node],parent)

def union(n1,n2,parent):
    #p1 = find(n1,parent)
    p2 = find(n2,parent)

    parent[n1]=p2

for n1,n2 in edges:
    union(n1,n2,parent)