# 13. Roman to Integer
class Solution:
    def romanToInt(self, s: str) -> int:
        m = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, }
        res = 0
        prev = m['M']
        for e in s:
            tmp = m[e]
            res += tmp
            if prev < tmp:
                res -= prev*2
            prev = tmp
        return res
