class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)
        for i, num in enumerate(nums):
            if i > 0 and num == nums[i-1]:
                continue
            if num > 0:
                break
            left = i+1
            right = n-1
            diff = -1*num
            while left < right:
                if nums[left] + nums[right] == diff:
                    res.append([num, nums[left], nums[right]])
                    left+=1
                    while nums[left] == nums[left-1] and left<right:
                        left+=1
                elif nums[left] + nums[right] > diff:
                    right -= 1
                else:
                    left +=1
                
        return res

        