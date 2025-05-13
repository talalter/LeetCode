class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows = len(matrix)
        cols = len(matrix[0])
        res = [[matrix[r][c] for r in range(rows)] for c in range(cols)]

        return res
        