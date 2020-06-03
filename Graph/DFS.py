from GraphAdjList import Graph

graph = Graph()
for node in range(7):
    graph.add_vertex(node)
graph.add_edge(0,1)
graph.add_edge(2,0)
graph.add_edge(1,2)
graph.add_edge(1,3)
graph.add_edge(4,2)
graph.add_edge(3,4)
graph.add_edge(4,5)
graph.add_edge(5,6)
# adj list of graph with 7 nodes:
# {0: [1, 2], 1: [0, 2, 3], 2: [0, 1, 4], 3: [1, 4], 4: [2, 3, 5], 5: [4, 6], 6: [5]}

'''
1. DFS func
2. loop through each nodes
3. if visited continue

1. DFS-visited
2. if not vitised: DF-visited
'''

def DFS_visited(node,adj_list,visited):
    print(node)
    children = adj_list[node]
    for child in children:
        if child not in visited:
            visited.add(child)
            DFS_visited(child,adj_list,visited)
def DFS(adj_list):
    visited = set()
    for node in adj_list:
        if node not in visited:
            visited.add(node)
            DFS_visited(node,adj_list,visited)
    print(visited)

DFS(graph.adjacent_list)
