class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        n = len(nums) - 1
        right = n
        res = [0] * len(nums)
        idx = n
        while left <= right:
            if abs(nums[left]) >= nums[right]:
                res[idx] = abs(nums[left])**2
                left += 1
            else:
                res[idx] = abs(nums[right])**2
                right -= 1  
            idx -= 1
        return res

