'''
union find by rank - rank/path compression
time - log(n)
1. init height = 1
2. get max height root
3. attach smaller onto larger. set larger height to max(curr_height,smaller+1)

4. path compression - immedaitely set find x root to new root that was found
'''


class Solution:
    def get_root(self, parent, node):
        prev = node
        nex = parent[node]

        while prev != nex:
            prev = nex
            nex = parent[prev]
        return nex

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # init var
        parent = [0] * (len(edges) + 1)
        # init height to 1
        height = {}
        for i in range(len(edges) + 1):
            height[i] = 1

        for i in range(len(edges) + 1):
            parent[i] = i

        # algorithm
        for edge in edges:
            n1, n2 = edge
            root_n1 = self.get_root(parent, n1)
            root_n2 = self.get_root(parent, n2)

            # path compression
            parent[n1] = root_n1
            parent[n2] = root_n2
            height[n1] = max(height[root_n1] - height[n1], height[n1] + 1)
            height[n2] = max(height[root_n2] - height[n2], height[n2] + 1)

            if root_n1 == root_n2: return edge

            '''
            # used to check path compression
            parent[root_n2] = root_n1
            print(parent)
            '''

            # union by rank
            larger = -1
            smaller = -1
            if height[root_n1] >= height[root_n2]:
                # print("yes")
                larger, smaller = root_n1, root_n2
            else:
                larger, smaller = root_n2, root_n1
            # print(larger,smaller)
            # stick the smaller tree onto larger tree
            parent[smaller] = larger
            # update height
            height[larger] = max(height[larger], height[smaller] + 1)

            # print(parent)
            # print(height)