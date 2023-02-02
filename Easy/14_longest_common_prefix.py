# 14. Longest Common Prefix
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n, m, res = min(strs), max(strs), 0
        for i in range(min(len(n), len(m))):
            if n[i] != m[i]:
                break
            else:
                res += 1
        return n[:res]
