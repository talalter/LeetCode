class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        
        i = 0
        while i <= len(haystack) - len(needle):
            if haystack[i] == needle[0]:
                j = 0
                while j < len(needle) and haystack[i + j] == needle[j]:
                    j += 1
                if j == len(needle):
                    return i
            i += 1
        return -1
