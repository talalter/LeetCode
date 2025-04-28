class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0 for _ in range(n)] for _ in range(n)]
        left, top = 0, 0
        right, bot = n, n
        val = 1
        while left < right and top < bot:
            for i in range(left, right):
                res[top][i] = val
                val += 1
            top += 1
            for i in range(top, bot):
                res[i][right-1] = val
                val += 1
            right -= 1
            for i in range(right-1, left-1, -1):
                res[bot-1][i] = val
                val += 1
            bot -= 1
            for i in range(bot-1, top-1, -1):
                res[i][left] = val
                val += 1
            left += 1
        return res