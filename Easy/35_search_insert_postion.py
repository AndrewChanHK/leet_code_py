# 35. Search Insert Position
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        res = -1

        for k, v in enumerate(nums):
            if v >= target:
                break
            else:
                res = k

        return res+1
