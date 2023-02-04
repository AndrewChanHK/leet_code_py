# 20. Valid Parentheses
class Solution:
    def isValid(self, s: str) -> bool:
        q = []

        for e in s:
            if e in m:
                q.append(m[e])
            elif not q or q.pop() != e:
                return False

        return not q


m = {
    '{': '}',
    '[': ']',
    '(': ')',
}
