'''
union find algorithm
######outline#######
var - use array to store parent of the node
1. loop each edge: n1,n2
    # check if n1 and n2 are in the same component. iterate up to the parent and see parent are the same
    set n1 parent to n2 parent. go up all the way until you hit the parent of each component. go until n1 and n2 equal the index
########
'''

class Solution:
    def get_root(self, parent, node):
        prev = node
        nex = parent[node]

        while prev != nex:
            prev = nex
            nex = parent[prev]
        return nex

    def findRedundantConnection(self, edges):
        # init var
        parent = [0] * (len(edges) + 1)

        for i in range(len(edges) + 1):
            parent[i] = i

        # algorithm
        for edge in edges:
            n1, n2 = edge
            root_n1 = self.get_root(parent, n1)
            root_n2 = self.get_root(parent, n2)
            # print(root_n1,root_n2)
            if root_n1 == root_n2: return edge
            # connect the nodes to the same component
            parent[root_n2] = root_n1
            # print(parent)