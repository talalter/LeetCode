class Solution:

 

    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:

        prev = lower - 1  # start from one less than lower
        res = []
        # Go through nums and one step beyond to capture the upper bound
        for i in range(len(nums) + 1):
            # Set curr to nums[i] if i is valid, otherwise set it to upper + 1
            curr = nums[i] if i < len(nums) else upper + 1

            if curr - prev >= 2:
                if prev + 1 == curr - 1:
                    res.append([prev + 1, prev + 1])
                else:
                    res.append([prev + 1, curr - 1])

            prev = curr

        return res
