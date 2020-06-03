'''
#####outline######
Try every node/numCourses
1. if any nodes have cycles then you return False
2. as soon as you find a cycle then you return False
In DFS must use three states
1. 0 = not visited
2. 1 = visited
3. -1 = cycle in current dfs
If you already visited you know there's no cycle
or
create list of in/out adj list
1. find all nodes with no incoming edges
2. put those nodes onto stack
3. pop off stack the items
Can you create a topological sort?
or
BFS
1. queue with no incoming edge
2. while queue.pop() if popped visited return
2. for all neighbors
3.  if no incoming edge then add to stack.

# the key to using queue for BFS and stack for DFS is that you remove from incoming list
and append node has no incoming edges!!!
##########
'''

# dfs solution
from collections import defaultdict
class Solution:
    def dfs(self, node, graph, visit):
        if visit[node] == -1:
            return False
        if visit[node] == 1:
            return True
        visit[node] = -1
        for nei in graph[node]:
            if not self.dfs(nei, graph, visit):
                return False
        visit[node] = 1
        return True


    def canFinish(self, numCourses: int, prerequisites: List[List[int]]):
        visited = {}
        graph = defaultdict(set)
        for course, req in prerequisites:
            graph[req].add(course)
        # create list of nodes to go through that have no incoming
        all_nodes = []
        for i in range(numCourses):
            all_nodes.append(i)
            visited[i] = 0
        # go through all nodes
        for node in all_nodes:
            if not self.dfs(node, graph, visited):
                return False
        return True

# DFS solution with stack and no recursion

class Solution:

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]):
        # values in prereq will only contain [0-(numCourses-1)]
        graph = defaultdict(set)
        incoming = defaultdict(set)
        # create adj list and neighbors list
        for course, pre in prerequisites:
            graph[pre].add(course)
            incoming[course].add(pre)
        # add nodes with no incoming edges to stack
        stack = []
        for node in range(numCourses):
            if node not in incoming:
                stack.append(node)
        print(stack)
        # algorithm
        count = 0
        while stack:
            node = stack.pop()
            count += 1
            # have node with no incoming edge
            # go through all outgoing nodes and remove node from incoming
            for out in graph[node]:
                incoming[out].remove(node)
                # print(incoming)
                if len(incoming[node]) == 0:
                    stack.append(out)
                    print(stack)
        print(count, numCourses)
        return count == numCourses

# BFS solution
from collections import defaultdict
from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]):
        graph = defaultdict(set)
        incoming = defaultdict(set)
        # set up adj list and incoming nodes list
        for course, req in prerequisites:
            graph[req].add(course)
            incoming[course].add(req)
        # no incoming edges
        queue = deque([])
        for node in range(numCourses):
            if node not in incoming:
                queue.append(node)
        visited = set()
        # BFS
        count = 0
        while queue:
            count += 1
            node = queue.popleft()
            visited.add(node)
            for nei in graph[node]:
                if nei in visited: return False
                incoming[nei].remove(node)
                if len(incoming[nei]) == 0:
                    queue.append(nei)

        return count == numCourses