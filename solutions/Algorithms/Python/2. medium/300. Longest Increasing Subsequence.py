class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        tails = [0] * len(nums)
        result = 0
        for num in nums:
            l, r = 0, result
            while l < r:
                mid = (l + r) // 2
                if tails[mid] < num:
                    l = mid + 1
                else:
                    r = mid
            result = max(result, l + 1)
            tails[l] = num
        return result
