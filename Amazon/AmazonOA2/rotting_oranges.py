from collections import deque


class Solution(object):
    def orangesRotting(self, grid):
        def is_fresh(r, c, grid):
            if (0 <= r <= len(grid) - 1 and (0 <= c <= len(grid[0]) - 1) and grid[r][c] == 1):
                return True
            return False

        queue = deque([])
        res = 0
        n = len(grid)
        m = len(grid[0])
        num_fresh = 0
        for r in range(n):
            for c in range(m):
                if grid[r][c] == 2:
                    queue.append([r, c])
                if grid[r][c] == 1:
                    num_fresh += 1

        dr = [0, 0, -1, 1]
        dc = [-1, 1, 0, 0]
        # c = dr.copy()
        if num_fresh == 0: return 0
        while queue:
            q = queue.copy()
            queue = deque([])
            print(q)
            while q:
                # queue = deque([])
                r, c = q.popleft()
                for i in range(len(dr)):
                    mv_r = r + dr[i]
                    mv_c = c + dc[i]
                    # if mv_r == 2: print("res")
                    if is_fresh(mv_r, mv_c, grid):
                        grid[mv_r][mv_c] = 2
                        queue.append([mv_r, mv_c])
                        num_fresh -= 1
            # queue = q[:]

            res += 1
            if num_fresh == 0: break
        return res if num_fresh == 0 else -1

        """
        :type grid: List[List[int]]
        :rtype: int
        """


'''
from collections import deque
class Solution(object):
    def orangesRotting(self, grid):
        def is_fresh(r,c,grid):
            if (0<=r<=len(grid)-1 and (0<=c<=len(grid[0])-1) and grid[r][c] == 1):
                return True
            return False
        
        
        queue = deque([])
        res = 0
        n = len(grid)
        m = len(grid[0])
        num_fresh =0
        for r in range(n):
            for c in range(m):
                if grid[r][c] == 2: 
                    queue.append([r,c])
                if grid[r][c] == 1:
                    num_fresh +=1
             
        dr = [0,0,-1,1]
        dc = [-1,1,0,0]
        #c = dr.copy()
        if num_fresh ==0:return 0
        while queue and num_fresh>0:
            res += 1
            for _ in range(len(queue)):
                r,c = queue.popleft()
                for i in range(len(dr)):
                    mv_r = r + dr[i]
                    mv_c = c + dc[i]
               
                    if is_fresh(mv_r,mv_c,grid):
                        grid[mv_r][mv_c] = 2
                        queue.append([mv_r,mv_c])
                        num_fresh -=1

        return res if num_fresh == 0 else -1
'''