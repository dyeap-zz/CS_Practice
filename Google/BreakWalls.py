'''
# https://leetcode.com/discuss/interview-question/353827/

[[0, 1, 0, 0, 0],
 [0, 0, 0, 1, 0],
 [1, 1, 0, 1, 0],
 [1, 1, 1, 1, 0]]


[[0, 1, 0, 0, 0],
 [0, 0, 0, 1, 0],
 [1, 1, 0, 1, 0],
 [1, 1, 1, 1, 0]]

what makes the wall broken different from rest?

brute force:
    break one wall and redo finding minsteps

remember that if you broke it then you would be there

if you hit wall update all nodes around and give it min dist
2
1. try flipping it to go from end to start

    if break bottom lest half you get same ans. but breaking the others give you different ans

need to memorize something to save time

log the path you are taking. for all cell break a wall and see if it take shorter to get
to get back along path


[[1, 1, 5, 6, 7],
 [2, 3, 4, 1, 8],
 [1, 1, 0, 1, 9],
 [1, 1, 1, 1, 10]]


max_num - curr_num - 1
[]

[[0, 1, 1],
 [1, 1, 0],
 [1, 1, 0]]

dict{[row,col]: old path it broke wall}

for each wall take max u/d/l/r to see if you can get shorter path.

Do it at the end along path

[[1, 1, 1, 1, 1],
 [2, 3, 4, 1, 1],
 [1, 4, 5, 1, 1],
 [1, 5, 6, 1, 0]]


if no path choose something along path to break and keep going wtih bfs on 0. if you hit number then done

'''
from collections import deque


def move_UDLR(pos,visited,queue,grid):
    curr_row,curr_col,elim,steps = pos[0], pos[1], pos[2],pos[3]
    num_rows = len(grid)
    num_cols = len(grid[0])

    for move in ([-1,0],[1,0],[0,-1],[0,1]):
        row = curr_row + move[0]
        col = curr_col + move[1]

        if row < 0 or row >= num_rows or col < 0 or col >= num_cols:
            continue

        elif grid[row][col] == 1 and elim > 0 and (row, col, elim - 1) not in visited:
            visited.add((row, col, elim-1))
            queue.append((row,col,elim-1,steps+1))

        elif grid[row][col] == 0 and (row, col, elim) not in visited:
            if row == num_rows-1 and col == num_cols -1:
                return steps + 1
            visited.add((row, col, elim))
            queue.append((row, col, elim,steps+1))
    return 0

def min_steps_maze(grid,k):
    if len(grid) == 0: return 0
    num_rows = len(grid)
    num_cols = len(grid[0])
    visited = set() # (row,col,elim,steps)
    queue = deque([(0,0,k,0)]) # (row,col,elim,steps)

    step = 0
    while queue:
        curr_queue = deque(queue)
        queue = []
        # try going up down l/r/d/u for each valid rc
        while curr_queue:
            pos = curr_queue.popleft()
            #visited[pos] = min_steps
            #row,col = rces[0], rces[1]
            steps = move_UDLR(pos,visited,queue,grid)
            if steps:
                print("got here")
                return steps

        #step += 1
        #if step == 8: break

    print(queue)
    print(visited)
    return -1


grid =[[0,0,1,0,0,0,0,1,0,1,1,0,0,1,1],[0,0,0,1,1,0,0,1,1,0,1,0,0,0,1],[1,1,0,0,0,0,0,1,0,1,0,0,1,0,0],[1,0,1,1,1,1,0,0,1,1,0,1,0,0,1],[1,0,0,0,1,1,0,1,1,0,0,1,1,1,1],[0,0,0,1,1,1,0,1,1,0,0,1,1,1,1],[0,0,0,1,0,1,0,0,0,0,1,1,0,1,1],[1,0,0,1,1,1,1,1,1,0,0,0,1,1,0],[0,0,1,0,0,1,1,1,1,1,0,1,0,0,0],[0,0,0,1,1,0,0,1,1,1,1,1,1,0,0],[0,0,0,0,1,1,1,0,0,1,1,1,0,1,0]]

print(min_steps_maze(grid,27))

'''

    [[1, 2, 3, 4, 5],
     [2, 3, 1, 1, 6],
     [1, 4, 5, 1, 1],
     [1, 1, 6, 7, 8]]



from collections import deque
class Solution:
    def shortestPath(self, grid, k) -> int:
        if len(grid) == 1 and len(grid[0]) == 1:
            return 0

        queue = deque([(0,0,k,0)])
        visited = set([(0,0,k)])

        if k > (len(grid)-1 + len(grid[0])-1):
            return len(grid)-1 + len(grid[0])-1

        while queue:
            row, col, eliminate, steps = queue.popleft()
            for new_row, new_col in [(row-1,col), (row,col+1), (row+1, col), (row, col-1)]:
                if (new_row >= 0 and
                    new_row < len(grid) and
                    new_col >= 0 and
                    new_col < len(grid[0])):
                    if grid[new_row][new_col] == 1 and eliminate > 0 and (new_row, new_col, eliminate-1) not in visited:
                        visited.add((new_row, new_col, eliminate-1))
                        queue.append((new_row, new_col, eliminate-1, steps+1))
                    if grid[new_row][new_col] == 0 and (new_row, new_col, eliminate) not in visited:
                        if new_row == len(grid)-1 and new_col == len(grid[0])-1:
                            return steps+1
                        visited.add((new_row, new_col, eliminate))
                        queue.append((new_row, new_col, eliminate, steps+1))

        return -1

sol = Solution()
sol.shortestPath(grid,4)

1. Do BFS but have an elimination variable that allows you to run BFS again
2. Always check wall first and add those to queue to ensure you return that ans first
3. if k is larger than num_rows-1 and num_cols-1 then return addition of values
4. In BFS use a queue not stack

'''