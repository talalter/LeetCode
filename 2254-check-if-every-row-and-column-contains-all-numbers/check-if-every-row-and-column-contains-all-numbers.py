class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        for row in range(n):
            row_set = [0] * n
            col_set = [0] * n
            for col in range(n):
                row_val = matrix[row][col]
                col_val = matrix[col][row]
                if row_val < 1 or row_val > n or row_set[row_val-1] == 1:
                    return False
                if col_val < 1 or col_val > n or col_set[col_val-1] == 1:
                    return False
                row_set[row_val-1] = 1 
                col_set[col_val-1] = 1
        return True
                

     
        return True