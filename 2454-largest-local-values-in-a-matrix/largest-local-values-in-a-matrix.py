class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        res = [[0]*(n-2) for _ in range(n-2)]

        for row in range(n-2):
            for col in range(n-2):
                max_num = 0
                for dr in range(row, row+3):
                    for dc in range(col, col+3):
                        if 0 <= dr < n and 0 <= dc < n:
                            max_num = max(max_num, grid[dr][dc])

                res[row][col] = max_num

        return res

        