class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        total_sum = 0
        n = len(mat)

        for row in range(n):
            for col in range(n):
                if row == col or row + col == n-1:
                    total_sum += mat[row][col]
        
        return total_sum