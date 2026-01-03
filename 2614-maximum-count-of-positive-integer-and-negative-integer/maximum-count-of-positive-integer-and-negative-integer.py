class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        
        def binary_search_positive(nums):
            left, right = 0, len(nums)-1
            while left <= right:
                mid = (left+right)//2
                if nums[mid] > 0 and (mid == 0 or nums[mid-1] <=0):
                    return mid
                if nums[mid] > 0:
                    right = mid - 1
                else:
                    left = mid + 1
            return -1
        def binary_search_negative(nums):
            left, right = 0, len(nums)-1
            while left <= right:
                mid = (left+right)//2
                if nums[mid] < 0 and (mid == len(nums)-1 or nums[mid + 1] >= 0):
                    return mid
                if nums[mid] < 0:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1
        neg = binary_search_negative(nums) + 1

        pos_idx = binary_search_positive(nums)
        pos = 0 if pos_idx == -1 else len(nums) - pos_idx  

        return max(neg, pos)