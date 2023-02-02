# 1. Two Sum
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        for k, v in enumerate(nums):
            r = target - v
            if r not in m:
                m[v] = k
            else:
                return m[r], k
