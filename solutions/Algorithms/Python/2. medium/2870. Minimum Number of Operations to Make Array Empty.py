from collections import Counter


class Solution:
    def minOperations(self, nums: list[int]) -> int:
        c = Counter(nums)
        res = 0
        for _, val in c.items():
            if val == 1:
                return -1
            elif val % 3 == 0:
                res += val // 3
            else:
                res += val // 3 + 1
        return res
