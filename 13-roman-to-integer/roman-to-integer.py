class Solution:
    def romanToInt(self, s: str) -> int:
        symbol_to_value = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }
        res = 0
        i = 0
        while i < len(s):
            if i+1 < len(s) and symbol_to_value[s[i]] < symbol_to_value[s[i+1]]:
                res = res + symbol_to_value[s[i+1]] - symbol_to_value[s[i]]
                i += 2
            else:
                res += symbol_to_value[s[i]]
                i+=1 
        return res