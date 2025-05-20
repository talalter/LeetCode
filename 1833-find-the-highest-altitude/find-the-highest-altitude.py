class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        current_sum = 0
        res = 0
        for num in gain:
            current_sum += num
            res = max(res, current_sum)
            
        return res
        