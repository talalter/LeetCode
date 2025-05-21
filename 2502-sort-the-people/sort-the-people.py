class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        height_to_names = {height : name for height, name in zip(heights, names)}

        return [height_to_names[height] for height in sorted(heights, key = lambda x: -x)]
 