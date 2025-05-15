class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        total_sum = 0
        n = len(mat)
        return sum(mat[row][col] for row in range(n) for col in range(n) if row == col or row + col == n-1)
