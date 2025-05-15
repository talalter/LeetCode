class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:

        rows = len(mat)
        cols = len(mat[0])
        ones_per_rows = [0] * rows
        for row in range(rows):
            ones = 0
            for col in range(cols):
                if mat[row][col] == 1:
                    ones += 1
            ones_per_rows[row] = ones
        current_max = 0
        current_index = 0
        for idx, amount in enumerate(ones_per_rows):
            if amount > current_max:
                current_max = amount
                current_index = idx

        return [current_index, current_max]


        