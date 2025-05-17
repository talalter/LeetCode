class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        target.sort()
        arr.sort()
        for t, a in zip(target, arr):
            if t != a:
                return False
        return True