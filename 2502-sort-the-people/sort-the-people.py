class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        height_to_names = {height : name for height, name in zip(heights, names)}
        heights.sort(key = lambda x: -x)
        res = []
        for height in heights:
            res.append(height_to_names[height])
        return res 