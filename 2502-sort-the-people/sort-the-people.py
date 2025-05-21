class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        height_to_names = {height : name for height, name in zip(heights, names)}
        heights.sort(key = lambda x: -x)
        res = [height_to_names[height] for height in heights]

        return res 