class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
                
            visited.add((r,c))

            if grid[r][c] == '0':
                return

            for dr, dc in directions:
                if (r + dr, c+dc) not in visited:
                    dfs(r + dr, c+dc)

        rows, cols = len(grid), len(grid[0])
        visited = set()
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        islands = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visited:
                    dfs(r, c)
                    islands += 1

        return islands
        