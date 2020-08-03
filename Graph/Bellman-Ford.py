negative edge weights. use Bellman ford

The idea is to start with starting node edge and update the distance.
The propogate through the rest of nodes.
You don't need to start with starting node edge. Order doesn't matter
The longest path possible is N-1

You can stop iterating when the distances have not changed
  5  5
1->2->3

must iterate at most twice. if you start with edge 2-3 and then do edge 1-2.
Then it must iterate N-1, twice to get final answer.
if you start with 1->2 then you only need one iteration. then next iteration, distance
array doesnt change

start
dist = [0,inf,inf]
iterate 1 do edge 2->3 then do edge 1->2
dist = [0,5,inf]
iterate 2
dist = [0,5,10]
max dist is the shortest distance from source to any node in graph or the longest path in
graph.


1. distance dict
2. start with sourceo of dist = 0
3. for 0 to N-1: must run for n-1 iterations, Since the longest path possible is N-1
4.      for times: all edges, a, b, w
5.          if dist[u] + w < dist[v]
6.              dist[v] = dist[u] + w
7.

must go though all edge N-1 times
time - O(E(V-1)) - O(VE)
space - O(V)

