# 118. Pascal's Triangle
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for i in range(1, numRows):
            nums = [x+y for x, y in zip([0]+res[i-1], res[i-1]+[0])]
            res.append(nums)
        return res
