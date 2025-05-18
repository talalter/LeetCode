from collections import defaultdict, Counter
class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        n = len(nums)

        flattened = [num for row in nums for num in set(row)]
        counter = Counter(flattened)
        return sorted([num for num, amount in counter.items() if amount == n])