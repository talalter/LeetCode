from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_dict = Counter(s)
        t_dict = Counter(t)
        for k, v in t_dict.items():
            if k not in s_dict or v!=s_dict[k]:
                return k
