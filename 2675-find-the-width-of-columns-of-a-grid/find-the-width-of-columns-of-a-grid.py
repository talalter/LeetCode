class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        def count_digits(num: int) -> int:
            return len(str(num))
            # num = abs(num)
            # counter = 0
            # while num > 0:
            #     num = num // 10
            #     counter += 1
            # return counter
        rows, cols = len(grid), len(grid[0])
        res = [1] * cols
        
        for row in range(rows):
            for col in range(cols):
                num = grid[row][col] 
                digits = count_digits(num)
                # if num < 0:
                #     digits += 1
                res[col] = max(res[col], digits)
        return res 