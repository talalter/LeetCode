class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        i = 0
        n = len(nums)
        while i < n:
            start = nums[i]
            while i + 1 < n and nums[i] + 1 == nums[i+1]:
                i+=1

            if nums[i] == start:
                res.append(f'{start}')
            else:
                res.append(f'{start}->{nums[i]}')
            i+=1
            
        return res 