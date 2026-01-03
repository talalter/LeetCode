from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        n_rows = len(grid)
        n_cols = len(grid[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0,-1)]
        num_islands = 0

        def bfs(r, c):

            queue = deque([(r, c)])
            while queue:
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c
                    if 0 <= nr < n_rows and 0 <= nc < n_cols and grid[nr][nc] == '1':
                        grid[nr][nc] = 0
                        queue.append((nr, nc))            
        
        for r in range(n_rows):
            for c in range(n_cols):
                if grid[r][c] == '1':
                    bfs(r, c)
                    num_islands += 1             
        return num_islands

