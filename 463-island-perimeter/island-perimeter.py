class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        

        def check_neighbors(row, col):
            directions = [[0,1],[1,0],[-1,0],[0,-1]]
            neighbors = 0
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                bound_row = 0 <= nr < rows
                bound_col = 0 <= nc < cols
                if bound_row and bound_col:
                    if grid[nr][nc] == 1:
                        neighbors += 1 
            return neighbors


        lands = 0
        total_neighbors = 0             
        
        rows = len(grid)
        cols = len(grid[0])
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    lands += 4
                    total_neighbors += check_neighbors(row, col)

        return lands - total_neighbors