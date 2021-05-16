'''
main points

1. create defaultdict of graph. can use a set
2. Create set of connections. order it by increasing order to quickly delete edge
3. in dfs
4. base case if visited -> return rank
5. set rank and res
6. loop all neighbors:
7. prevent from going to parent
8. dfs(nei,depth+1)
9. if nei depth is smaller than current depth a cycle was found so delet in set
10. compare depth and return the smaller of each

'''
import collections

def criticalConnections(n, connections):
    # create graph: {node:list of neighbors}
    def makeGraph(connections):
        graph = collections.defaultdict(list)
        for conn in connections:
            graph[conn[0]].append(conn[1])
            graph[conn[1]].append(conn[0])
        return graph


    graph = makeGraph(connections)
    connections = set(map(tuple, (map(sorted, connections))))
    # used to easily remove edges if you sort them and add to a set.
    # Thus (low,high) edge
    '''
    # same as above line
    def sortConnections(self, connections):
    sortedConnections = set()
    
    for conn in connections:
        conn.sort()
        sortedConnections.add((conn[0], conn[1]))
    
    return sortedConnections
    '''
    # set rank do -2 because when you start with 0,0 then you don't want dfs to go back to parent
    rank = [-2] * (n+1)

    def dfs(node, depth):
        # if node already visited
        if rank[node] >= 0:
            # visiting (0<=rank<n), or visited (rank=n)
            return rank[node]
        rank[node] = depth
        # max dfs depth you can get is number of nodes
        min_back_depth = n
        for neighbor in graph[node]:
            if rank[neighbor] == depth - 1:
                continue  # don't immmediately go back to parent. that's why i didn't choose -1 as the special value, in case depth==0.
            # go to neighbor and ranking
            back_depth = dfs(neighbor, depth + 1)
            # this means there's a cycle. so delete edge
            if back_depth <= depth:
                connections.discard(tuple(sorted((node, neighbor))))
            # need to keep track of min depth to return
            min_back_depth = min(min_back_depth, back_depth)
        rank[node] = n  # this line is not necessary. see the "brain teaser" section below
        return min_back_depth

    dfs(1, 0)  # since this is a connected graph, we don't have to loop over all nodes.
    return list(connections)


def findCriticalConn():
    def dfs(d):
        print(a)

    a = 9
    dfs(3)
    return []

serversNum = 4
connectionsNum = 4
connections = [[1, 2], [1, 3], [3, 2], [3, 4]]

print(criticalConnections(serversNum, connections))

findCriticalConn()



print([3,1].sort())

from collections import defaultdict


def findCriticalConn(serversNum, connectionsNum, connections):
    def dfs(node, curr_d):
        if depth[node] >= 0:
            return depth[node]

        depth[node] = curr_d
        min_depth = serversNum
        for nei in g[node]:
            # don't go back to parent
            if depth[nei] == curr_d - 1: continue

            back_depth = dfs(nei, curr_d + 1)

            # visited and has it's a cycle
            if back_depth <= curr_d:
                rem = [node, nei]
                rem.sort()
                sorted_c.remove(tuple(rem))
            min_depth = min(back_depth,min_depth)
        return min_depth

    sorted_c = []
    for edge in connections:
        edge.sort()
        sorted_c.append(tuple(edge))

    g = defaultdict(set)
    for n1, n2 in connections:
        g[n1].add(n2)
        g[n2].add(n1)

    depth = [-100 for _ in range(serversNum+1)]
    dfs(1, 0)
    return sorted_c


serversNum = 4
connectionsNum = 4
connections = [[1, 2], [1, 3], [3, 2], [3, 4]]

print(findCriticalConn(serversNum, connectionsNum, connections))