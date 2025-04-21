class Solution:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        n = len(grid)
        mid = n // 2
        y_values = [0, 0, 0]
        not_y_values = [0, 0, 0]
        res = float('inf')
        for r in range(n):
            for c in range(n):
                if (r == c and r <= mid) or (r + c == n - 1 and r <= mid)or (r > mid and c == mid):
                    y_values[grid[r][c]] += 1
                else:
                    not_y_values[grid[r][c]] += 1
        
        total_y = sum(y_values)
        total_not_y = sum(not_y_values)
        res = float('inf')

        # Try all pairs of (y_digit, not_y_digit) where they are different
        for y_digit in range(3):
            for not_y_digit in range(3):
                if y_digit != not_y_digit:
                    changes = (total_y - y_values[y_digit]) + (total_not_y - not_y_values[not_y_digit])
                    res = min(res, changes)

        return res
