class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        arr = [0] * n**2
        for row in range(n):
            for col in range(n):
                arr[grid[row][col]-1] += 1
        res = [0, 0]
        for i in range(n**2):
            if arr[i] == 0:
                res[1] = i+1
            if arr[i] == 2:
                res[0] = i+1
        return res

        