class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        counter = dict()
        n = len(nums)
        for row in nums:
            for num in row:
                if num in counter:
                    counter[num] += 1
                else:
                    counter[num] = 1
        
        return sorted([num for num, amount in counter.items() if amount == n])