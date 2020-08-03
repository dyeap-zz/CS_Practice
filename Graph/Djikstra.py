from collections import deque, defaultdict


class Solution:

    def networkDelayTime(self, times, N: int, K: int) -> int:
        graph = defaultdict(set)
        dist = {}
        visited = set()
        for o, i, t in times:
            graph[o].add((i, t))

        for node in range(1, N + 1):
            dist[node] = float('inf')

        dist[K] = 0
        queue = deque([(K, 0)])
        while queue:
            node, time = queue.popleft()
            for nei, w in graph[node]:
                dist[nei] = min(dist[nei], time + w)
            visited.add(node)
            # get lowest distance
            cand_dist = float('inf')
            cand_node = -1
            for node, d in dist.items():
                if node not in visited and d < cand_dist:
                    cand_node, cand_dist = node, d

            if cand_node == -1: break
            queue.append((cand_node, cand_dist))

        return max(dist.values()) if len(visited) == N else -1

times = [[2,1,1],[2,3,1],[3,4,1]]
N = 4
K = 2
sol = Solution()

print(sol.networkDelayTime(times,N,K))


# djikstra's using a heap
'''
 1. Use distance to log down final distance to a node. Also use as visited
2. Use pq to track next node to process
3. While pq:
    1. Pop off heap
    2. If node has been visited: continue
    3. Add node distance dict/visited
    4. For all nei
        1. If nei not visited:
            1. Add to pq

'''
from collections import deque, defaultdict
import heapq

class Solution:

    def networkDelayTime(self, times, N: int, K: int) -> int:
        dist = {}
        graph = defaultdict(set)
        for o, i, t in times:
            graph[o].add((i, t))

        heap = [(0, K)]
        while heap:
            d, node = heapq.heappop(heap)
            if node in dist: continue
            dist[node] = d
            for nei, d2 in graph[node]:
                if nei not in dist:
                    heapq.heappush(heap, (d + d2, nei))

        return max(dist.values()) if len(dist) == N else -1

sol = Solution()

print(sol.networkDelayTime(times,N,K))

for every node must find the min dist to process next
naive implementation
time - O(N^2 + E)
space -

must create graph going through all edges for E
The priority queue is log N for pop and push.
For every node you must pop and push log N
so run time is N log N

pq implementation
time - O(N log N + E)
space - O(N+E)
