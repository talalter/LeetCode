class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_to_indices = dict()
        for index, num in enumerate(nums):
            if num in diff_to_indices:
                return [index, diff_to_indices[num]]
            diff_to_indices[target-num] = index

        