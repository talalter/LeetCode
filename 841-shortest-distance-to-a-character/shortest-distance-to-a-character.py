from typing import List

class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        # First Pass - Identify the positions of 'c'
        appearances = [idx for idx, char in enumerate(s) if char == c]

        # Initialize the result array with maximum distances
        res = [float('inf')] * len(s)

        # First Pass - Calculate distances to the closest 'c' to the left
        for i in range(len(s)):
            for pos in appearances:
                res[i] = min(res[i], abs(i - pos))
        
        return res

# Example Usage:
s = "loveleetcode"
c = "e"
print(Solution().shortestToChar(s, c))  # Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
