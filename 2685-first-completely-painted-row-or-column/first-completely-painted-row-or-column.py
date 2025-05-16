class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        val_to_indices = dict()
        rows = len(mat)
        cols = len(mat[0])
        for row in range(rows):
            for col in range(cols):
                val_to_indices[mat[row][col]] = (row, col)
        
        painted_rows = [0] * rows
        paintet_cols = [0] * cols
        for i, val in enumerate(arr):
            row, col = val_to_indices[val]
            painted_rows[row] += 1
            paintet_cols[col] += 1
            if painted_rows[row] == cols or paintet_cols[col] == rows:
                return i
