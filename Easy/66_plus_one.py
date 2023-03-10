# 66. Plus One
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        for i in range(len(digits) - 1, -1, -1):
            digits[i] += 1

            if digits[i] > 9:
                digits[i] %= 10
            else:
                return digits

        digits.insert(0, 1)
        return digits
