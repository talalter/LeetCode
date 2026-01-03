from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n_rows = len(grid)
        n_cols = len(grid[0])
        total_minutes = 0
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        queue = deque()
        visited = set()
        for row in range(n_rows):
            for col in range(n_cols):
                if grid[row][col] == 2:
                    queue.append((row, col))
                    visited.add((row, col))
        while queue:
            rotten_this_round = False
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (nr, nc) not in visited and 0 <= nr < n_rows and 0 <= nc < n_cols and grid[nr][nc] == 1:
                        rotten_this_round = True
                        grid[nr][nc] = 2
                        queue.append((nr, nc))
                        visited.add((nr, nc))
            if rotten_this_round:
                total_minutes += 1 

        for row in range(n_rows):
            for col in range(n_cols):
                if grid[row][col] == 1:
                    return -1
        
        return total_minutes
