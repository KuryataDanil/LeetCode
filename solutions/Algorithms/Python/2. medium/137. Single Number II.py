from collections import Counter
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        c = Counter(nums)
        for key, value in c.items():
            if value == 1:
                return key
        return -1
