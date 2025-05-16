from typing import List

class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)

        # Check rows
        for i in range(n):
            for j in range(n):
                val = abs(matrix[i][j])
                # Out of range or already marked
                if val < 1 or val > n or matrix[i][val - 1] < 0:
                    return False
                # Mark as visited by negating
                matrix[i][val - 1] = -matrix[i][val - 1]

            # Restore the row
            for j in range(n):
                matrix[i][j] = abs(matrix[i][j])

        # Check columns
        for j in range(n):
            for i in range(n):
                val = abs(matrix[i][j])
                # Out of range or already marked
                if val < 1 or val > n or matrix[val - 1][j] < 0:
                    return False
                # Mark as visited by negating
                matrix[val - 1][j] = -matrix[val - 1][j]

            # Restore the column


        return True
