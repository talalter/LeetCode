class NeighborSum:

    def __init__(self, grid: List[List[int]]):
        n = len(grid)
        self.diag = dict()
        self.adj = dict()
        adj_dirt = ((0, 1), (1,0), (-1, 0), (0, -1))
        diag_dirt = ((-1, -1), (1, 1), (-1, 1), (1,-1))
        for row in range(n):
            for col in range(n):
                sum_adj = 0
                sum_diag = 0
                for dr, dc in adj_dirt:
                    nr, nc = dr + row, dc + col
                    if 0<=nr<n and 0<=nc<n:
                        sum_adj += grid[nr][nc]

                for dr, dc in diag_dirt:
                    nr, nc = dr + row, dc + col
                    if 0<=nr<n and 0<=nc<n:
                        sum_diag += grid[nr][nc]

                self.adj[grid[row][col]] = sum_adj
                self.diag[grid[row][col]] = sum_diag
     

        

    def adjacentSum(self, value: int) -> int:
        return self.adj[value]

    def diagonalSum(self, value: int) -> int:
        return self.diag[value]


# Your NeighborSum object will be instantiated and called as such:
# obj = NeighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)