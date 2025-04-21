class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        counter = dict()
        for num in nums:
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1
        for _, a in counter.items():
            if a > 2:
                return False
        
        return True
