from collections import defaultdict
class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        counter = defaultdict(int)
        n = len(nums)
        for row in nums:
            for num in row:
                counter[num] += 1

        
        return sorted([num for num, amount in counter.items() if amount == n])