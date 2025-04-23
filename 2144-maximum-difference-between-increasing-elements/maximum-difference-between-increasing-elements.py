class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        max_diff = -1
        min_number = nums[0]
        for num in nums[1:]:
            min_number = min(min_number, num)
            max_diff = max(max_diff, num - min_number)
        return -1 if max_diff == 0 else max_diff