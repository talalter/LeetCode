from typing import List

class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        found = False
        
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                if found:
                    return False
                found = True

                # Check if removing nums[i] or nums[i-1] maintains strict increase
                # Skip the current element if possible
                if i == 1 or nums[i] > nums[i - 2]:
                    continue
                # Skip the previous element
                elif i == len(nums) - 1 or nums[i + 1] > nums[i - 1]:
                    continue
                else:
                    return False

        return True

# Example Usage:
print(Solution().canBeIncreasing([1, 2, 10, 5, 7]))  # Output: True
print(Solution().canBeIncreasing([2, 3, 1, 2]))      # Output: False
