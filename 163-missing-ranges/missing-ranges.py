class Solution:

 

    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        def format_range(start: int, end: int) -> str:
            if start == end:
                return [start, start]
            else:
                return [start, end]
        result = []
        prev = lower - 1  # start from one less than lower

        # Go through nums and one step beyond to capture the upper bound
        for i in range(len(nums) + 1):
            # Set curr to nums[i] if i is valid, otherwise set it to upper + 1
            curr = nums[i] if i < len(nums) else upper + 1

            if curr - prev >= 2:
                result.append(format_range(prev + 1, curr - 1))

            prev = curr

        return result
