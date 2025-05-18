class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        n = len(nums)
        def binary_search(flag:bool) -> int:
            left, right = 0, n-1
            while left<=right:
                mid = (left + right) //2
                if flag:
                    if nums[mid] > 0:
                        right = mid - 1
                    else :
                        left = mid + 1
                else:
                    if nums[mid] < 0:
                        left = mid + 1
                    else :
                        right = mid - 1
                    
            if flag:
                return left
            return right
        
        negative = binary_search(False)
        positive = binary_search(True)
        num_negatives = negative + 1
        num_positives = n - positive
        return max(num_negatives, num_positives)

                