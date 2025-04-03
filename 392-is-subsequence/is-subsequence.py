class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        length = len(s) - 1
        if length < 0:
            return True
        for letter in t:
            if letter == s[i]:
                i+=1
            if i>length:
                return True

        return False
        