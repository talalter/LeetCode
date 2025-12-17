class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        s_nums = set(nums)
        for i in range(1, len(nums)+1):
            if i not in s_nums:
                res.append(i)
        return res