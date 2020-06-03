class Graph():
    def __init__(self):
        self.num_nodes = 0
        self.adjacent_list = {}

    def add_vertex(self,node):
        adj_list = self.adjacent_list
        if node in adj_list:
            return
        else:
            adj_list[node] = []
            self.num_nodes += 1
    def add_edge(self, node1, node2):
        adj_list = self.adjacent_list
        if (node1 in adj_list and node2 in adj_list):
            node1_conn = adj_list[node1]
            if not node1 in node1_conn:
                node1_conn.append(node2)
                adj_list[node1] = node1_conn

            node2_conn = adj_list[node2]
            if not node2 in node2_conn:
                node2_conn.append(node1)
                adj_list[node2] = node2_conn

        else:
            print("One of the nodes not in dictionary")

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
a = 2

