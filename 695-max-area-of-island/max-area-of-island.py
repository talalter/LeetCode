class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n_rows = len(grid)
        n_cols = len(grid[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0,-1)]
        current_area = 0

        def bfs(r, c):

            area = 1   
            queue = deque([(r, c)])
            grid[r][c] = 0
            while queue:
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c
                    if 0 <= nr < n_rows and 0 <= nc < n_cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 0
                        area += 1
                        queue.append((nr, nc))     

            return area  
        
        for r in range(n_rows):
            for c in range(n_cols):
                if grid[r][c] == 1:
                    area = bfs(r, c)
                    current_area = max(current_area, area)           
        return current_area

