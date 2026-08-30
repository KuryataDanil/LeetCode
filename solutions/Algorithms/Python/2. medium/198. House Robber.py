class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums)

        def dp(i, nums: list[int], cache: dict[int]):
            # base case
            if len(nums) - 2 <= i < len(nums):
                return nums[i]
            if i >= len(nums) - 1:
                return 0
            if i in cache:
                return cache[i]

            rob_next_2 = dp(i + 2, nums, cache)
            rob_next_3 = dp(i + 3, nums, cache)

            max_n = max(rob_next_2, rob_next_3)
            cache[i] = max_n + nums[i]

            return max_n + nums[i]

        cache = dict()
        return max(dp(0, nums, cache), dp(1, nums, cache))
