class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        n_rows = len(grid)
        n_cols = len(grid[0])
        visited = set()
        directions = [(1, 0), (0, 1), (-1, 0), (0,-1)]
        num_islands = 0

        def dfs(r, c):

            if (r<0 or r >= n_rows or c<0 or c >= n_cols or grid[r][c] == '0' or (r, c) in visited):
                return
            
            visited.add((r, c))

            for dr, dc in directions:
                if (r+dr, c+dc) not in visited:
                    dfs(r+dr, c+dc)
            
        
        for r in range(n_rows):
            for c in range(n_cols):
                if grid[r][c] == '1' and (r, c) not in visited:
                    dfs(r, c)
                    num_islands += 1             
        return num_islands

