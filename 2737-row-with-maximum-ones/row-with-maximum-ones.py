class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:

        rows = len(mat)
        cols = len(mat[0])
        max_ones = 0
        current_index = 0
        for row in range(rows):
            ones = 0
            for col in range(cols):
                if mat[row][col] == 1:
                    ones += 1
            if ones > max_ones:
                max_ones = ones
                current_index = row

        return [current_index, max_ones]


        